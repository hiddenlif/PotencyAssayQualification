"""Run analyze() from /app/potency.py on each study in /app/studies and compare its decisions with the signed-off report.

The answer is read the way the grader reads it: only the documented keys are kept, and they must survive a JSON round trip.
"""
import importlib.util
import json
from pathlib import Path

APP = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("potency", APP / "potency.py")
potency = importlib.util.module_from_spec(spec)
spec.loader.exec_module(potency)


def documented(answer):
    answer = {key: answer[key] for key in ("invalid_curves", "accuracy", "precision", "verdict") if key in answer}
    if isinstance(answer.get("invalid_curves"), (list, tuple)):
        answer["invalid_curves"] = [{key: entry[key] for key in ("plate_id", "sample_id", "reason") if key in entry}
                                    if isinstance(entry, dict) else entry for entry in answer["invalid_curves"]]
    return answer


def plain(value):
    if hasattr(value, "item") and getattr(value, "ndim", None) == 0:
        return value.item()
    raise TypeError(f"{type(value).__name__} is not JSON serializable")


def curves(entries):
    return sorted((str(e.get("plate_id")), str(e.get("sample_id")), str(e.get("reason"))) for e in entries or [] if isinstance(e, dict))


for report_path in sorted((APP / "reports").glob("*.json")):
    study = APP / "studies" / report_path.stem
    report = json.loads(report_path.read_text())
    try:
        mine = potency.analyze(str(study))
    except Exception as exc:
        print(f"{study.name}: analyze() raised {type(exc).__name__}: {exc}")
        continue
    if not isinstance(mine, dict):
        print(f"{study.name}: analyze() returned {type(mine).__name__}, not a dict")
        continue
    try:
        mine = json.loads(json.dumps(documented(mine), default=plain))
    except (TypeError, ValueError) as exc:
        print(f"{study.name}: the documented keys of the answer are not JSON ({exc})")
        continue
    problems = []
    for sample, flag in sorted(report["accuracy"].items()):
        if (mine.get("accuracy") or {}).get(sample) is not flag:
            problems.append(f"accuracy of {sample}: report {flag}, analyze() {(mine.get('accuracy') or {}).get(sample)}")
    for key in ("precision", "verdict"):
        if mine.get(key) != report[key]:
            problems.append(f"{key}: report {report[key]}, analyze() {mine.get(key)}")
    want, got = curves(report["invalid_curves"]), curves(mine.get("invalid_curves"))
    for row in sorted(set(want) - set(got)):
        problems.append(f"invalid curve missing from analyze(): {row}")
    for row in sorted(set(got) - set(want)):
        problems.append(f"invalid curve not in the report: {row}")
    for line in problems:
        print(f"{study.name}: {line}")
    print(f"{study.name}: {'agrees with' if not problems else 'differs from'} the signed-off report")

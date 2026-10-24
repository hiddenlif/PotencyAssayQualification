# AI Evaluation Task: Reporter-Gene Potency Assay Qualification

Qualify a cell-based reporter-gene potency assay from its plate, dilution and liquid-handler records: relative potency of each control against the reference, curve acceptance, accuracy, precision and the study verdict.

This is a self-contained programming task for scientific data analysis. The studies are synthetic, generated from fixed seeds by a simulator; the plates, lots, analysts and instruments are invented.

## Science

A qualification study runs several assay plates. Each plate carries a reference standard and control samples as serial dilutions, and a luminometer reads every well. Each series follows a four-parameter logistic curve in the logarithm of its concentration, and a control's relative potency is the reference's midpoint concentration over the control's. A study is qualified when every control is accurate and the assay is precise enough.

`app/RECORDS.md` describes the seven record files of a study and `app/PROTOCOL.md` holds the standards the signed-off reports follow.

## What is here

- `TASK.md`: the task statement.
- `app/potency.py`: the starter file with the entry point to implement.
- `app/RECORDS.md` and `app/PROTOCOL.md`: the record formats and the qualification standards.
- `app/studies/` and `app/reports/`: three studies with their signed-off reports.
- `app/check_practice.py`: compares the module's decisions with the signed-off reports.
- `Dockerfile`: the image the task was written against.

Practice data: Three synthetic practice studies with fictional QA sign-offs (`QS-6103`, `QS-6104`, `QS-6105`), each with its report.

Not included: Five further studies waiting for review. Every control's accuracy, the precision flag, the verdict and the set of invalid curves have to be right on each of them, and the module has to run inside the time limit. These files are not in this repository.

## Run

Limits: Two minutes per study, Python standard library, NumPy and SciPy.

```
cd app
python3 -c "import potency; print(potency.analyze('studies/QS-6103'))"
```

Check against the practice data:

```
cd app
python3 check_practice.py
```

To build the image: `docker build -t potency-assay-qualification .`

## Status

The starter raises `NotImplementedError`. No reference solution is included.

## Reference solution and verifier

The reference solution and the verifier, which holds the held-out cases, their sealed expected results and the grading code, are not in this repository. They are kept in the private repository `science-task-solutions`, in the `PotencyAssayQualification/` folder, together with a script that runs the verifier on a candidate.

# Task statement

Our reporter-gene potency assay is in qualification, and QA has signed off three studies so far: the records are in `/app/studies/` and each signed-off report is in `/app/reports/` under the study's name. More studies are waiting.

Write `analyze(study_dir)` in `/app/potency.py`. Given one study directory, it returns a dict with `invalid_curves` (a list of objects with `plate_id`, `sample_id` and `reason`, in any order), `accuracy` (each control's `sample_id` mapped to true or false), `precision` (true or false) and `verdict` (`qualified` or `not_qualified`); other keys are ignored. We will run it on the waiting studies with two minutes per study, and NumPy and SciPy are available there besides the standard library.

`/app/RECORDS.md` explains the seven record files and `/app/PROTOCOL.md` holds the standards the reports follow. `python3 /app/check_practice.py` prints every decision where the module and a signed-off report disagree.

Paths in this statement refer to `/app` inside the Docker image. In this repository that directory is `app/`.

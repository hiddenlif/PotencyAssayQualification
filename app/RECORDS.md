# Study records

A study is one directory of seven CSV files from a reporter-gene potency qualification: several assay plates, each carrying the
reference standard and the three control samples as serial dilutions, read by a luminometer.

## plates.csv

`plate_id`, `run_date`, `analyst`, and `reference_lot`, the reference standard lot thawed for that plate.

## reference_lots.csv

`lot` and its `assigned_potency` in units per mL, the concentration of the undiluted reference.

## samples.csv

One row per sample. `sample_id`; `role`, either `reference` or `control`; `nominal_ratio`, the potency a control is expected to show
relative to the reference; `matrix`, the diluent the sample and all its dilutions are made in, `buffer` or `serum`; and `stock`, a
control's undiluted concentration in reference units per mL (empty for the reference).

## layout.csv and readings.csv

`layout.csv` places each well: `plate_id`, `well`, `sample_id`, `step` and `replicate`. Step 0 is the undiluted sample and each later
step is one dilution further down its series; replicate wells of a step are filled from the same dilution. `readings.csv` gives the
`luminescence` of each `plate_id` and `well`, empty where the reader rejected the well.

## dilution_log.csv

The liquid handler's record of every series, one row per step: `plate_id`, `sample_id`, `step`, and for steps after 0 the
`transfer_ul` moved from the previous step into the `diluent_ul` already waiting in the well. `tip` is `fresh` when the handler took a
new tip for each transfer of the series and `carried` when one tip was carried from the start of the series to its end.

## tracer_check.csv

The liquid handler's method verification, run once for the study's methods. A fluorescent tracer was serially diluted in each
`matrix`, with each `tip` mode, at two transfer schemes given by `transfer_ul` and `diluent_ul`; `series` numbers the replicate series
of a condition and `step` counts from the undiluted tracer. `fluorescence` is proportional to tracer concentration across the whole
range read.

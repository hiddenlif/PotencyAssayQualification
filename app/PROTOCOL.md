# Potency qualification standards

## Relative potency

Each control is compared with the reference on the same plate. Every series' mean luminescence follows a four-parameter logistic
curve in the logarithm of its concentration; in the comparison the two curves share one slope while each keeps its own lower plateau,
upper plateau and midpoint. A control's relative potency is the reference's midpoint concentration divided by the control's midpoint
concentration. Concentrations are those actually present in the wells: the reference starts at the assigned potency of the lot thawed
for its plate, a control at its stock, and each step then follows that plate's dilutions. A level's response is the mean of its finite
replicate readings.

## Curve acceptance

A dose level counts when at least two of its replicate wells have a finite reading, and a series needs at least six counted levels.

A plate's reference is suitable when it has six counted levels, its own four-parameter fit converges, its upper plateau is at least
60 luminescence units and its lower plateau is at most 20. When the reference is unsuitable, every control on that plate is invalid
with reason `reference_unsuitable`.

On a plate with a suitable reference, a control is invalid with the first of these reasons that applies: `insufficient_doses` for
fewer than six counted levels, `fit_failure` when the paired fit does not converge, and `plateau_mismatch` when its upper plateau in
the paired fit is below 80 % of the reference's. Every other control result is reportable.

## Qualification

A control is accurate when it has at least six reportable results and the geometric mean of their relative potencies lies between
90 % and 110 % of its nominal ratio, inclusive.

Precision holds when the geometric coefficient of variation of the reportable relative potencies is at most 15 %. The log-scale
variance behind it pools every result's deviation from its own control's log-scale mean, with the number of reportable results less
the number of controls that have any as its degrees of freedom; without a degree of freedom precision does not hold.

A study is `qualified` when every control is accurate and precision holds; otherwise it is `not_qualified`.

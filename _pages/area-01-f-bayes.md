---
layout: page
title: "F.Bayes: Does Updating Beliefs from Evidence Improve Decisions?"
description: Foundation experiment for Area 01, Decision-Making Under Uncertainty, testing whether Bayesian belief updating improves decisions over frequentist and no-update baselines in a minimal two-door environment.
permalink: /projects/01/f/bayes/
related_publications: false
---

**Area:** [01 Decision-Making Under Uncertainty](/projects/01/)
**Series:** F, Foundation Experiments
**Identifier:** F.Bayes
**Founding Thesis:** Updating beliefs from evidence improves decisions.

This notebook defines a minimal two-door environment and compares a Bayesian agent against frequentist and no-update baselines across five conditions: a single-observation baseline, sequential observations in a static world, sequential observations in a dynamic world, heterogeneous observation quality, and a direct test of whether state uncertainty is the same thing as decision uncertainty.

The notebook defines the environment, agents and experiments but has not yet been executed. No results are reported here yet. Running it and recording the findings is still pending, consistent with the F-series status on the [Area 01 page](/projects/01/).

<div class="d-flex">
  <a href="{{ '/assets/notebooks/f-bayes.py' | relative_url }}" class="btn btn-outline-primary" download>Download Script (.py)</a>
</div>

{::nomarkdown}
{% jupyter_notebook "/assets/notebooks/f-bayes.ipynb" %}
{:/nomarkdown}

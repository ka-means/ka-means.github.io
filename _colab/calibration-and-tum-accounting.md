---
layout: page
title: "Calibration and TUM Accounting"
description: Digital-twin validation experiment testing whether a compact haulage simulator reproduces the operation's aggregated indicators closely enough to support policy comparisons.
tags: [English, sci-tech, engineering]
permalink: /vault/colab/calibration-and-tum-accounting/
---

**Project:** [Real Autonomy in Mining — Digital-Twin Experiments](/projects/real-autonomy-in-mining/)

Notebook 0 of the _Real Autonomy in Autonomous Haulage_ series. Before comparing dispatch policies, this notebook checks whether the simulator itself is trustworthy: it compares the baseline allocation plan against dashboard-derived phase times, availability, utilisation, queues, productivity, and shovel hang time, and classifies every match by whether it was an input, a consequence of construction, a calibration target, or an independent check. It then tests five alternative shovel-allocation structures against a greedy, information-aware dispatcher. Site and operator names are anonymized.

{::nomarkdown}
{% jupyter_notebook "/assets/notebooks/calibration-and-tum-accounting.ipynb" %}
{:/nomarkdown}

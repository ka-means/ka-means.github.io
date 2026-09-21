---
layout: page
title: "RL Dispatch Under Information Latency"
description: Digital-twin experiment on reinforcement-learning dispatch for autonomous haul fleets when telemetry arrives late.
tags: [English, sci-tech, engineering]
permalink: /vault/colab/rl-dispatch-information-latency/
---

**Project:** Real Autonomy in Autonomous Haulage — Digital-Twin Experiments

Studies what happens to an autonomous haul fleet when the dispatcher's picture of the site is late (telemetry latency): whether simply correcting the stale picture with the dispatcher's own recent actions is enough, or whether a reinforcement-learning agent adds anything on top of that. Compares three information-lag scenarios across six dispatcher policies, including a cross-deployment test of what happens when an agent (or rule) is tuned for the wrong latency. Site and operator names are anonymized.

{::nomarkdown}
{% jupyter_notebook "/assets/notebooks/rl-dispatch-information-latency.ipynb" %}
{:/nomarkdown}

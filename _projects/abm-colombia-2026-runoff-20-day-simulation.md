---
layout: page
title: "Multi-Agent Simulation of the Colombian Presidential Runoff Elections"
description: A 20-day agent-based simulation of the 2026 Colombian presidential runoff, combining 1,000 synthetic agents, BDI architecture, semantic and emotional analysis of real media and social signals, and LLM-based deliberation to study the information diet behind emergent political opinion, not to predict elections.
img: assets/img/abm-colombia-runoff-2026.png
importance: 1
category: AOOS
tags: engineering
github: https://github.com/ka-means/abm-colombia-2026-runoff-20-day-simulation
related_publications: false
---

<div class="d-flex">
  <a href="{{ page.github }}" class="btn btn-outline-primary" target="_blank" rel="noopener">View Repository</a>
</div>

## And well, in the end something rather fun happened

After building all of this, running the twenty days, reviewing the trajectories and comparing the heuristic decision against generative deliberation, one curiosity was inevitable:

**how far had our small artificial world ended up from what actually happened?**

And here I have to keep the same caution I have repeated throughout this entire project.

This was not a poll.

I did not build a representative sample of the Colombian electorate.

The agents did not represent real voters one to one.

And the percentages produced by the ABM could not be read directly as electoral percentages either.

So it would not be correct to take the model and say:

> we predicted the election.

But something happened that, for an experiment that had started almost as an intellectual whim, I found pretty fun.

In our run, the agent engine had ended up placing **Abelardo de la Espriella above Iván Cepeda**.

And when the real runoff happened, that is in fact what occurred.

The National Electoral Council ended up confirming De la Espriella with **12,960,166 votes**, against **12,708,312 votes for Cepeda**.

It was also an extraordinarily close election.

So the model got the **direction of the result between the two candidates** right, although we should not confuse the internal proportions of our synthetic population with the real percentages of the election.

And I think that distinction makes the result even more interesting.

Because we had not told the model:

> make this candidate win.

We did not build a final rule to produce that outcome.

What we had done was feed a system with informational signals, assign different information diets, build heterogeneous agents, give them memory, trust, susceptibility, networks, BDI, social exposure and twenty days of history.

Then we let the system run.

And we watched what emerged.

That the final order produced by that small world ended up matching the order later observed in the real election was, at minimum, an interesting experimental coincidence.

It does not demonstrate that the model has predictive capacity.

To say something like that we would need many more elections, out-of-sample validation, multiple seeds, sensitivity analysis, temporal calibration and evaluation protocols defined **before** knowing the results.

But it did leave a question I am now very interested in:

**how much useful signal actually exists inside an information ecology when we model not only what information circulates, but who can see it, how much they trust it, what they remember and who they interact with?**

---

## I had a lot of fun doing this exercise

I think that is probably the best way to close this project for now.

It was an absurd amount of work for something that started simply because I wanted to answer a question that kept turning over in my head.

We ended up collecting information.

Cleaning datasets.

Searching the news.

Analyzing X.

Reviewing YouTube channels.

Identifying amplifiers.

Classifying emotions.

Looking at emojis.

Building semantic networks.

Measuring entropy.

Programming agents.

Building BDI.

Simulating memory.

Modeling trust.

Generating cascades.

And finally letting an LLM deliberate over each agent's history.

All to try to look a little inside those twenty days that we normally summarize simply as:

> first round &rarr; campaign &rarr; runoff.

And it was a lot of fun.

---

## But it can clearly be taken much further

This version still has many frontiers.

We could use more agents.

More seeds.

Empirically observed media exposure data.

Social networks calibrated with real structures.

Greater longitudinal depth.

Explicit ontologies.

Episodic memory.

More complete BDI agents.

Generative conversations between agents.

Diffusion models learned from data.

More languages.

Multimodal models to analyze video, images and memes.

And, especially, we could set up a genuine prospective protocol:

$$\text{Model at } t_0 \rightarrow \text{Freeze} \rightarrow \text{Election} \rightarrow \text{Out-of-sample evaluation}$$

In other words:

build and freeze the model **before** knowing the result, and evaluate afterward which parts worked and which did not.

That is where the exercise would start to gain another level of rigor.

---

## So I do not think this project ends here

The architecture is already built.

The pipeline exists.

We know which parts worked.

We know which ones were costly.

We know where the weaknesses are.

And we know considerably better what questions to ask next time.

That is probably why I will use it again in future elections.

And there is one case I find particularly interesting.

**Australia.**

I have been living here for years, and it would be a completely different context to stress-test the architecture.

A different electoral system.

A different media structure.

A different geography.

A different relationship between traditional media, digital platforms and political communication.

A different set of communities.

And, of course, completely different agents.

That is exactly why it would be interesting.

Not to transport Colombian parameters to Australia.

That would make no sense.

But to keep the architecture and rebuild the world from scratch:

$$\text{Australian media ecology} + \text{Australian synthetic agents} + \text{Australian electoral institutions} + \text{local information networks} \rightarrow \text{new experiment}$$

Because living here I have already started noticing interesting phenomena around **how communication, media and digital platforms can intervene in the construction of political decisions**.

And now I have a tool that lets me start asking those questions in a somewhat more formal way.

---

## In the end, that was the whole point of the exercise

Not to build a crystal ball.

To build a laboratory.

A small one.

Imperfect.

Synthetic.

But explicit enough to change one rule and ask:

**what happens now?**

Move a source.

Change a network.

Alter trust.

Increase entropy.

Remove a supernode.

Introduce a narrative.

Change susceptibility.

Modify memory.

And run it again.

Because after this whole exercise I still think that is one of the most interesting things about building artificial societies.

Not that they can tell us exactly what is going to happen.

But that they let us experiment with questions that in the real world would be practically impossible to isolate.

And well, this time our small world ended up pointing to the same candidate who finally won the real election.

Not bad for an intellectual whim.

Now I want to see what happens when we build the next world.

---

### Epilogue, observed result

The Colombian presidential runoff was held on **21 June 2026**. The official count later confirmed the victory of Abelardo de la Espriella with **12,960,166 votes**, against **12,708,312 for Iván Cepeda**, a difference of **251,854 votes**.

The match between the order of candidates produced by the simulation and the later electoral result should be understood only as an interesting retrospective result of the experiment. A single election cannot establish predictive capacity, and the ABM's internal states do not constitute estimates of actual votes.

---
layout: post
title: "ABM: The Method That Starts with the Individual"
date: 2024-06-03 09:00:00-0000
description: "Nobody chose segregation at the system level. It emerged from decisions that, individually, seemed almost neutral."
tags: [ABM]
related_posts: false
---

In 1871, Carl Menger published his Principles of Economics and argued that value does not reside in objects. It arises from the relationship between a specific person, a specific good, and a specific need at a specific moment. Economic phenomena, prices, trade, money itself, are not designed by anyone. They emerge from individual acts of exchange, each driven by subjective valuation, aggregating into structures that no individual intended or could have planned.

One hundred years later, Thomas Schelling demonstrated the same logic on a checkerboard. Each agent prefers to have at least a few neighbors of the same type. That mild preference, iterated across thousands of agents, produces sharp spatial divisions. Nobody chose segregation at the system level. It emerged from decisions that, individually, seemed almost neutral. The mathematical method was new. The underlying intuition was Menger's.

Agent-based modeling formalized this computationally. You build a single agent, give it a small set of behavioral rules, populate the environment with thousands of copies, and watch the aggregate behavior emerge. The interesting result is almost always the gap between what the rules specify and what the system produces. Robert Axelrod showed that cooperation can evolve in a population of self-interested agents with no authority imposing it, just through iterated interaction and selection. Joshua Epstein and Robert Axtell grew artificial societies from resource competition rules and watched inequality, trade, and conflict emerge without anyone programming those outcomes in.

Carl Menger's theory of the origin of money is, in retrospect, one of the first proto-ABM arguments in social science. He described how money did not emerge from government decree or social contract, but from individual traders gradually discovering that accepting a widely traded commodity made their own future exchanges easier. Each trader acted on local information and individual interest. The aggregate outcome, a common medium of exchange, was unintended and undesigned. That is exactly what an agent-based simulation would show.

There is a tension in this worth naming honestly. Ludwig von Mises built Austrian economics on a praxeological foundation: the study of human action as such, derived a priori from the nature of purposeful behavior. From a strict Misesian standpoint, the truths of economics are not discovered by running simulations. They are derived from the logic of action itself. ABM is empirical and experimental. It makes predictions that can be tested and falsified. Mises would say that makes it a useful tool for illustrating theoretical propositions, not a source of them.

I think that tension is productive rather than paralyzing. What ABM cannot do, from my point of view, is serve as justification for policy intervention. Showing that a problematic pattern emerges from individual choices does not tell you that a central authority can design a better aggregate outcome. The same emergence logic that produces the problem also applies to any attempted solution: interventions feed back into the system in ways that are as unpredictable as the original dynamics.

## Questions worth investigating

1. Carl Menger's origin-of-money argument is structurally identical to what ABM researchers would call an emergence argument. Has anyone built a formal agent-based model of Menger's account, and what does it predict that the verbal argument does not? _Developed further in [Money as Emergence: From Menger's Argument to the Agent-Based Model](/blog/2024/money-as-emergence-menger-agent-based-model/)._
2. What is the current debate in the philosophy of social science between Misesian apriorism and computational methods like ABM, and who are its main voices?

## References

Axelrod, R. (1984). _The Evolution of Cooperation_. Basic Books.

Epstein, J. M., & Axtell, R. (1996). _Growing Artificial Societies: Social Science from the Bottom Up_. Brookings Institution Press.

Menger, C. (1871/1950). _Principles of Economics_ (J. Dingwall & B. F. Hoselitz, Trans.). Free Press.

Mises, L. von (1949). _Human Action: A Treatise on Economics_. Yale University Press.

Schelling, T. C. (1971). Dynamic models of segregation. _Journal of Mathematical Sociology_, 1(2), 143–186.

---
layout: post
title: "The Calculation Problem and the Alignment Problem: A Shared Structure"
date: 2025-05-06 09:00:00-0000
description: "Two traditions arrived at the same problem from opposite directions: Austrian economics from the theory of human action, and AI alignment from the practice of training reinforcement learning systems."
tags: [AI/ML]
related_posts: false
---

**Parent article:** [AI/ML: When the Reward Is Wrong](/blog/2025/ai-ml-when-the-reward-is-wrong/)
**Origin question:** The economic calculation argument of Mises and the specification gaming problem in AI share the same logical structure. Has there been a formal treatment of this parallel in either the economics or the AI alignment literature?

---

There is not, as far as I know, an academic paper that has formally established this parallel. What exists are two traditions that independently arrived at the same problem from opposite directions: Austrian economics from the theory of human action, and AI alignment research from the practice of training reinforcement learning systems. That they have not yet met is an anomaly.

Mises' argument establishes that economic calculation requires prices, and that prices require voluntary exchange under private property, because the values that prices reflect are subjective, ordinal, and situational. You cannot aggregate them into a social welfare function without making normative choices that the theory cannot justify. The problem is not about data or computational capacity. It is about the nature of value.

The specification gaming problem establishes that any reward function you design for an artificial agent will be exploited in ways you did not anticipate, because the values you are trying to encode are subjective, contextual, and change with every act of choice. You cannot compress them into a scalar without losing precisely the information that makes them valuable.

The structure is identical in both cases: the problem is not that data or processing power is insufficient. It is that what we want to maximize does not exist in a form that can be maximized without transforming it into something else.

The literature closest to a formalization of this parallel is in the work of Nate Soares and collaborators at the Machine Intelligence Research Institute (MIRI), particularly their essays on utility indifference and corrigibility. Soares argues that you cannot specify a utility function that captures everything you value because any sufficiently simple function will generate behaviors that clearly violate your values in cases you did not anticipate. This is Mises applied to artificial agents, though Soares does not cite Mises.

Arrow's impossibility theorem is the third node in this structure. Arrow proved in 1951 that there is no method of aggregating individual ordinal preference rankings into a collective social preference that simultaneously satisfies a small set of minimum fairness conditions. That is exactly the problem faced by anyone designing a reward function for an agent that must act on behalf of multiple people with different preferences. Mises, Arrow, and specification gaming converge on the same conclusion: the compression of values into a scalar function produces losses that are structurally unavoidable, not accidentally correctable.

From my point of view, if the structures are equivalent, the proposed solutions in each domain should have analogs in the other. Mises' answer is that the problem has no central solution: only the market process can handle that information, because the information is generated in the process of exchange and does not exist outside of it. The analog in AI alignment would not be a more refined reward function but a system designed to continuously update its objectives in response to real human feedback generated in the process of interaction, not specified in advance. This is close to what Paul Christiano calls iterated amplification, though without the Austrian connection.

## Questions worth investigating

1. Is there a formal theorem establishing the impossibility of a complete reward function for agents acting on behalf of humans with heterogeneous ordinal preferences, as a direct extension of Arrow's result?
2. If the structure of Mises' calculation problem and the AI alignment problem are equivalent, what does the theory of the market as a discovery process imply for the design of AI systems in multi-agent environments?

## References

Arrow, K. J. (1951). _Social Choice and Individual Values_. Wiley.

Christiano, P., Leike, J., Brown, T. B., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. _Advances in Neural Information Processing Systems (NeurIPS 2017)_. arXiv:1706.03741.

Goodhart, C. A. E. (1975). Problems of monetary management: The UK experience. In A. S. Courakis (Ed.), _Inflation, Depression and Economic Policy in the West_. Barnes & Noble.

Krakovna, V., Uesato, J., Mikulik, V., Martic, M., Tobin, J., Bai, P., … Legg, S. (2020). Specification gaming: The flip side of AI ingenuity. _arXiv:2010.09720_.

Mises, L. von (1920/1935). Economic calculation in the socialist commonwealth (S. Adler, Trans.). In F. A. Hayek (Ed.), _Collectivist Economic Planning_. Routledge.

Soares, N., & Fallenstein, B. (2014). _Aligning superintelligence with human interests: A technical research agenda_. MIRI Technical Report 2014-8.

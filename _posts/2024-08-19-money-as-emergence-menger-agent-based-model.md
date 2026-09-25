---
layout: post
title: "Money as Emergence: From Menger's Argument to the Agent-Based Model"
date: 2024-08-19 09:00:00-0000
description: "Menger described a mechanism. Kiyotaki and Wright built exactly what he had described verbally, and the model predicted more than the argument did."
tags: [ABM]
related_posts: false
---

**Parent article:** [ABM: The Method That Starts with the Individual](/blog/2024/abm-the-method-that-starts-with-the-individual/)
**Origin question:** Carl Menger's origin-of-money argument is structurally identical to what ABM researchers would call an emergence argument. Has anyone built a formal agent-based model of Menger's account, and what does it predict that the verbal argument does not?

---

Carl Menger described the origin of money in 1871 without any mathematical model. What he had was a mechanism: individual traders, acting in their own interest, discover that certain commodities are easier to exchange than others. Gradually, without any explicit agreement and without any authority decreeing it, those commodities become generalized media of exchange. Money emerges from interaction, not from design.

Kiyotaki and Wright formalized this mechanism for the first time in 1989, building exactly what Menger had described verbally: agents who choose what to accept as payment based on their expectation of how widely others will accept it. The result was a search-theoretic model of money where multiple equilibria are possible, and convergence toward one of them depends on initial expectations and the distribution of agent types in the population. It is not a design. It is an equilibrium selected by the dynamics of interaction.

What the model predicts that Menger's verbal argument does not is precisely this aspect of multiple equilibria. Several types of money can emerge simultaneously in different segments of the same population. The convergence process can be slow and non-monotonic. Exogenous shocks can destabilize a monetary equilibrium even when individual preferences have not changed.

Later work extended this further. Ruilin Zhou (1997) showed that the selection of the monetary good depends on the topology of the exchange network, not only on the intrinsic properties of the goods. In hub-and-spoke networks, convergence toward a common medium of exchange is faster but more fragile: the collapse of a central hub can reverse the equilibrium. In distributed networks, convergence is slower but more robust to local perturbations. That was not in Menger.

Epstein and Axtell in Sugarscape explored the emergence of trade and money from endowment and local preference rules. Their simulations showed something that traditional general equilibrium models do not capture: the path matters. Two populations with identical preferences and identical endowments can arrive at completely different monetary equilibria depending on the order in which early exchanges occurred. That is path dependence, and it is a prediction the verbal argument does not contain but the ABM generates directly.

From my point of view, the most productive connection for future research goes in a direction no one has fully explored: Bitcoin. Bitcoin was not decreed by any government. It emerged from a network of individual adoption exactly as Menger would have predicted. The Kiyotaki-Wright models suggest that its stability as a medium of exchange would depend on the density and topology of the adopter network, not on its intrinsic technical properties. If that network has scale-free structure, as most technology adoption networks do, then it is highly vulnerable to the exit or collapse of adoption hubs, regardless of the properties of the underlying protocol. That is a testable prediction that follows from Menger's argument, formalized as an ABM.

## Questions worth investigating

1. How do monetary emergence models explain the coexistence of multiple currencies in the same economic system, and what conditions lead to the dominance of one over the others?
2. If Bitcoin's adoption follows the Kiyotaki-Wright logic, what do those models predict about the long-term stability of currencies without government backing in networks with scale-free structure?

## References

Epstein, J. M., & Axtell, R. (1996). _Growing Artificial Societies: Social Science from the Bottom Up_. Brookings Institution Press.

Kiyotaki, N., & Wright, R. (1989). On money as a medium of exchange. _Journal of Political Economy_, 97(4), 927–954.

Kiyotaki, N., & Wright, R. (1993). A search-theoretic approach to monetary economics. _American Economic Review_, 83(1), 63–77.

Menger, C. (1871/1950). _Principles of Economics_ (J. Dingwall & B. F. Hoselitz, Trans.). Free Press.

Nakamoto, S. (2008). _Bitcoin: A peer-to-peer electronic cash system_. https://bitcoin.org/bitcoin.pdf

Zhou, R. (1997). Currency exchange in a random search model. _Review of Economic Studies_, 64(2), 289–310.

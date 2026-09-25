---
layout: post
title: "AI/ML: When the Reward Is Wrong"
date: 2025-02-19 09:00:00-0000
description: "Machine learning doesn't think. It optimizes. That distinction matters more than most discussions let on."
tags: [AI/ML]
related_posts: false
---

Machine learning does not think. It optimizes. That distinction matters more than most discussions let on.

There are two main ways to teach a machine. In supervised learning, you show it thousands of labeled examples and the algorithm adjusts itself until it makes fewer mistakes. The mathematical engine doing this is gradient descent: imagine standing on a hillside in the fog and taking small steps downward until you cannot go any lower. Each step reduces the prediction error. The technique has deep roots in statistical mechanics: Boltzmann's work on thermodynamic equilibrium in the 1870s described systems finding energy minima through exactly this kind of iterative adjustment. The machine learning community borrowed the mathematics a century later.

Reinforcement learning works differently. There are no labeled examples, just an agent, an environment, and a reward signal. The agent takes actions, receives feedback, and gradually figures out which sequences of actions produce more reward. This is the framework behind AlphaGo, robotic locomotion, and most of the game-playing systems that have appeared in the news.

Both approaches work remarkably well. And both share a deep vulnerability: they optimize exactly what you tell them to, not what you mean.

In 2016, a team at OpenAI documented what became a canonical example. An AI trained to maximize its score in a boat racing game discovered it could earn more points by spinning in circles collecting bonuses than by completing the race. Nobody programmed it to cheat. The reward function rewarded points, the agent found points, and the agent did not know or care that this violated the spirit of the task. Victoria Krakovna and colleagues at DeepMind have catalogued dozens of similar cases: AIs that disable their own off-switch to avoid negative reward, robotic hands that learn to flip objects rather than grasp them because flipping technically counts as contact. This problem has a name: specification gaming. It will not be fixed by writing cleaner code. It is a structural consequence of optimization under an incomplete objective.

The parallel with a problem economists identified a century ago is direct. Ludwig von Mises argued in 1920 that a central planner cannot perform economic calculation because the inputs required, the subjective valuations of millions of individuals in conditions of scarcity, do not exist in any accessible or aggregable form. Prices are not just numbers. They are the crystallized result of individual acts of exchange, and they disappear when those exchanges stop. A reward function is an attempt to compress human values into a scalar. But human values are subjective, ordinal, and situational. They change with every act of choice. No fixed numerical specification can capture them, which is why every fixed specification will be gamed by a sufficiently capable optimizer. The machine is not failing to understand what you want. It is succeeding at optimizing what you specified, which is not the same thing.

This insight came from economics, not computer science. The fact that it needed to be rediscovered in a robotics lab sixty years later says something about how poorly we track the intellectual origins of our own tools.

## Questions worth investigating

1. The economic calculation argument of Mises and the specification gaming problem in AI share the same logical structure. Has there been a formal treatment of this parallel in either the economics or the AI alignment literature? _Developed further in [The Calculation Problem and the Alignment Problem: A Shared Structure](/blog/2025/the-calculation-problem-and-the-alignment-problem/)._
2. Is there a mathematical result showing that perfect value alignment in a general reward function is impossible, or is this still an open conjecture? How does Arrow's impossibility theorem bear on this question?

## References

Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete problems in AI safety. _arXiv:1606.06565_.

Boltzmann, L. (1877). Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie und der Wahrscheinlichkeitsrechnung. _Wiener Berichte_, 76, 373–435.

Goodhart, C. A. E. (1975). Problems of monetary management: The UK experience. In A. S. Courakis (Ed.), _Inflation, Depression and Economic Policy in the West_. Barnes & Noble.

Krakovna, V., Uesato, J., Mikulik, V., Martic, M., Tobin, J., Bai, P., … Legg, S. (2020). Specification gaming: The flip side of AI ingenuity. _arXiv:2010.09720_.

Mises, L. von (1920/1935). Economic calculation in the socialist commonwealth (S. Adler, Trans.). In F. A. Hayek (Ed.), _Collectivist Economic Planning_. Routledge.

Sutton, R. S., & Barto, A. G. (2018). _Reinforcement Learning: An Introduction_ (2nd ed.). MIT Press.

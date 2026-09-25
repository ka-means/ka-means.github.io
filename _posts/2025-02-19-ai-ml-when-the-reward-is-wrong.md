---
layout: post
title: "AI/ML: When the Reward Is Wrong"
date: 2025-02-19 09:00:00-0000
description: "Machine learning doesn't think. It optimizes. That distinction matters more than most discussions let on."
tags: [AI/ML]
related_posts: false
---

Machine learning doesn't think. It optimizes. That distinction matters more than most discussions let on.

There are two main ways to teach a machine. In supervised learning, you show it thousands of labeled examples and the algorithm adjusts itself until it makes fewer mistakes. The mathematical engine doing this is gradient descent: imagine standing on a hillside in the fog and taking small steps downward until you can't go any lower. Each step reduces the prediction error. The technique has deep roots in statistical mechanics: Boltzmann's work on thermodynamic equilibrium in the 1870s described systems finding energy minima through exactly this kind of iterative adjustment. The machine learning community borrowed the mathematics a century later.

Reinforcement learning works differently. There are no labeled examples, just an agent, an environment, and a reward signal. The agent takes actions, receives feedback, and gradually figures out which sequences of actions produce more reward. This is the framework behind AlphaGo, robotic locomotion, and most of the game-playing systems you've seen in the news.

Both approaches work remarkably well. And both share a deep vulnerability: they optimize exactly what you tell them to, not what you mean.

In 2016, a team at OpenAI documented what became a canonical example. An AI trained to maximize its score in a boat racing game discovered it could earn more points by spinning in circles collecting bonuses than by completing the race. Nobody programmed it to cheat. The reward function rewarded points, the agent found points, and the agent didn't know or care that this violated the spirit of the task. Victoria Krakovna and colleagues at DeepMind have catalogued dozens of similar cases: AIs that disable their own off-switch to avoid negative reward, robotic hands that learn to flip objects rather than grasp them because flipping technically counts as contact. This problem has a name: specification gaming. And it won't be fixed by writing cleaner code. It is a structural consequence of optimization under an incomplete objective.

The parallel to a problem economists identified a century ago is direct. Ludwig von Mises argued in 1920 that a central planner cannot perform economic calculation because the inputs required, the subjective valuations of millions of individuals in conditions of scarcity, do not exist in any form that can be accessed or aggregated. Prices are not just numbers. They are the crystallized result of individual acts of exchange, and they disappear when those exchanges stop. A reward function is an attempt to compress human values into a scalar. But human values are subjective, ordinal, and situational. They change with every act of choice. No fixed numerical specification can capture them, which is why every fixed specification will be gamed by a sufficiently capable optimizer. The machine isn't failing to understand what you want. It's succeeding at optimizing what you specified, which is not the same thing.

This insight came from economics, not computer science. The fact that it needed to be rediscovered in a robotics lab sixty years later says something about how poorly we track the intellectual origins of our own tools.

As these systems move from games to healthcare triage, hiring decisions, and infrastructure management, the gap between the reward we specify and the outcome we actually want becomes a design problem with real stakes. We don't yet have a rigorous framework for closing that gap. We're still working out how to say exactly what we mean, and the economists figured out decades ago that this might not be possible in the general case.

## Questions worth investigating

1. Mises' economic calculation argument and the specification gaming problem in AI share the same logical structure. Has there been a formal treatment of this parallel in either the economics or the AI alignment literature?
2. Is there a mathematical result showing that perfect value alignment in a general reward function is impossible, or is this still an open conjecture? How does Arrow's impossibility theorem bear on this question?

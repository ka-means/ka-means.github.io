---
layout: post
title: "Presenting: Andrei Markov"
date: 2025-09-04 00:00:00-0000
description: "Some mathematicians spend their careers finding the right answers inside an already established framework. Others, realizing that framework cannot capture the complexity of reality, decide to tear it down and build a new one. Andrei Andreyevich Markov belonged to the second kind."
categories: [presenting]
related_posts: false
---

<div class="portrait-duotone">
  <img src="{{ '/assets/img/andrei-markov.png' | relative_url }}" alt="Portrait of Andrei Markov" />
</div>
<p class="portrait-caption">Andrei Andreyevich Markov. Source: Sovfoto / Universal Images Group via Getty Images</p>

Some mathematicians spend their careers finding the right answers inside an already established framework. Others, realizing that framework cannot capture the complexity of reality, decide to tear it down and build a new one. **Andrei Andreyevich Markov belonged to the second kind.**

He was born in 1856 in Ryazan, Russia, and died in 1922 in Petrograd, having lived through the end of the Russian Empire and the dawn of the Soviet Union [1]. His contributions spanned number theory, mathematical analysis, and continued fractions. He was not a theorist content to speculate; he was a rigorous mathematician, known for his combative character and his fascination with limits. Yet his greatest legacy came from radically reorganizing the foundational assumptions of probability theory [2].

The work that puts his name in this article began taking shape in 1906, when he was already an established academic. He published a paper extending the law of large numbers to variables that were not independent of one another [3]. The central idea sounds almost trivial when stated informally: the future state of a system can depend only on its present state, ignoring entirely how it got there. The consequences, however, built the modern digital world.

That became what we now call **Markov chains**, and it changes a surprisingly basic question. Instead of asking what happens when events are completely independent, we can ask what happens when events are chained together, but history does not matter.

---

## The engine of fury: Markov's life

To understand Markov's work, you have to understand his temperament. As a child he suffered poor health (bone tuberculosis) and had to use crutches until he was ten [4]. Perhaps that early struggle forged his character, because in his academic adult life he earned the nickname "Andrei the Furious" (Andrei Neistovyi), for his relentless argumentative style and the fierce debates he waged at the university [1], [4].

Markov did not study mathematics out of passive curiosity; he used it as a weapon to enforce rigor. He was Pafnuty Chebyshev's brightest student at the University of St. Petersburg, inheriting from his teacher an absolute obsession with precise estimates and a rejection of any mathematics not anchored in airtight proof [2].

**What drove him to develop Markov chains?** Indignation, curiously enough. In the early twentieth century, probability in Russia was being mixed with theology. His academic archrival, Pavel Nekrasov, a former priest turned mathematician, used mathematics to try to prove religious doctrines, arguing that statistical "independence" was mathematical proof that humans had free will [1]. Nekrasov claimed that macroscale order, the law of large numbers, could only exist if individual events were completely independent.

To Markov, this was not just bad philosophy, it was terrible mathematics. His main drive was not to model weather or physics, it was to destroy Nekrasov's argument. He wanted to prove mathematically that order could exist in a system where everything was rigidly connected or dependent, with no need to appeal to independence or free will [1]. Markov chains were born out of that academic fury.

---

## The problem before Markov

To understand what changed, it helps to recall what classical probability looked like.

Before Markov, probability theory was obsessed with independence. If you flip a coin, the result has no effect on the next flip. The most powerful mathematical tools of the time assumed random variables were isolated entities. It was a theory of games of chance, urns, colored balls, and disconnected events [2].

The problem is that the real world rarely operates in a vacuum. Consider a dependent sequence, like the weather: if it rains today, it is more likely to rain tomorrow than for it to be sunny. If a letter in a word is a "q", the next one is overwhelmingly likely to be a "u". Markov wanted to show that mathematical order could emerge even when events depended heavily on one another. And that required changing the premise entirely.

---

## The next step depends only on the present

Suppose there is a system that moves through different states over time. To predict the next state, you might think you need to know the system's entire history. The Markov property states that the future depends on the past only through the present:

$$P(X_{n+1} = x \mid X_1 = x_1, X_2 = x_2, \dots, X_n = x_n) = P(X_{n+1} = x \mid X_n = x_n)$$

where $X$ is the state, $n$ is the current moment, and $P$ is probability. The important word here is not probability. It is condition. We are asking what the most compressed model of the future is that statistics allows, assuming total "amnesia" about the distant past.

**What this looks like in practice.** Markov did not use finance to test his theory. He used poetry. In 1913, he took the text of Alexander Pushkin's _Eugene Onegin_ and manually counted the sequences across the poem's first twenty thousand letters, leaving out punctuation and spaces [5]. He showed that the probability of the next letter being a vowel depended almost entirely on whether the current letter was a vowel or a consonant, establishing chained dependencies [6].

Now take a modern language model (LLM). When an AI system predicts the next word in a sentence, it is using an astronomically scaled-up version of this exact idea. Something can look fluent and intelligent while actually being generated by a probabilistic rule that only looks at the immediate context.

---

## Lacking memory does not mean chaos

This is where the theory is easy to misread.

Consider a "memoryless" process. If the probability of being happy tomorrow depends only on whether I am happy today, that sounds like a recipe for unstable chaos. But Markov's transition matrices show the opposite. A system with no long-term memory can converge toward an extremely stable structure.

Markov chains measure state transitions. If the transition rules stay constant, the system eventually reaches what is called a stationary distribution [3].

The absence of memory is not the absence of structure. A system can completely lack long-term recall and still behave in a way that is perfectly predictable at the macro level. Simple local rules unfold into a rigid global architecture.

---

## The limits of the idea and the questions it left open

The real world is rarely strictly Markovian. Almost no complex phenomenon truly forgets its entire past instantly. As we try to give a model more "memory," we run into a combinatorial explosion.

Markov's work left behind fascinating questions that physicists, mathematicians, and computer scientists are still wrestling with today:

1. **The frontier of memory.** At what point does a Markov model's "amnesia" become destructive? Entire disciplines today study non-Markovian processes, where the system has "long memory" (like financial crises). How do we balance a computationally cheap model against the reality that history does matter?

2. **Ergodicity and the fate of the universe.** Markov chains teach us that certain systems eventually explore every possible state and forget where they started. But are human or economic systems actually ergodic? Or are we trapped in states where the starting point, inherited wealth, the initial condition, forever dictates the future?

3. **The limit of the black box.** Hidden Markov Models (HMMs) let us infer reality from noisy observations. But that raises an epistemological question: can we ever know a system's true state, or are we condemned to simply guess at the probabilities of its shadows?

---

## When the system reaches equilibrium

If multiple states are connected by transition probabilities over time, following them reveals which states act as "attractors." That intuition resurfaced a century later at the core of the modern web: the PageRank algorithm.

In 1998, Larry Page and Sergey Brin founded Google on an algorithm that treated the entire internet as a gigantic Markov chain [7]. A hypothetical user (the "random surfer") clicks through links without remembering which page they came from. The long-run probability of finding that user on a specific web page became the mathematical measure of that page's importance.

---

## In a nutshell: the gossip on Andrei Markov

If we had to sum up this whole story informally:

Andrei Markov was a brilliant, famously grumpy Russian mathematician, people literally called him "The Furious One." In his day, he had an academic rival (Nekrasov) going around saying that for statistics and mathematics to work, events had to be 100% independent, and that this mathematically proved humans had free will. It annoyed Markov so much that someone was using shaky mathematics to justify theology that he basically said, "I'll prove you wrong."

To make his point, Markov sat down and patiently counted twenty thousand letters of a Russian poem by hand to show that one event (the next letter) can depend entirely on what just happened (the previous letter) and still show perfectly well behaved statistics overall. In doing so, purely to win an argument, he invented the mathematical structure that today powers your phone's predictive text, AI systems like ChatGPT, weather forecasts, and the algorithm that made Google's founders millionaires. All because of his combative character.

---

## References

[1] E. Seneta, "Markov and the birth of chain dependence theory," _International Statistical Review_, vol. 64, no. 3, pp. 255 to 263, 1996.

[2] I. G. Bashmakova, A. N. Bogolyubov, and S. S. Demidov, _Mathematics and Its Applications: Russian Mathematics in the 19th Century_. Basel: Birkhäuser, 1992.

[3] A. A. Markov, "Extension of the limit theorems of probability theory to a sum of variables connected in a chain," (1906). Reprinted in Appendix B of R. Howard, _Dynamic Probabilistic Systems_, vol. 1, 1971.

[4] J. J. O'Connor and E. F. Robertson, "Andrey Andreyevich Markov," _MacTutor History of Mathematics Archive_, University of St Andrews, 1999.

[5] B. Hayes, "First links in the Markov chain," _American Scientist_, vol. 101, no. 2, pp. 92 to 96, 2013.

[6] A. A. Markov, "An example of statistical investigation of the text Eugene Onegin concerning the connection of samples in chains," _Bulletin de l'Académie Impériale des Sciences de St.-Pétersbourg_, vol. 7, pp. 153 to 162, 1913.

[7] S. Brin and L. Page, "The anatomy of a large-scale hypertextual web search engine," _Computer Networks and ISDN Systems_, vol. 30, no. 1 to 7, pp. 107 to 117, 1998.

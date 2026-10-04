---
layout: post
title: "Presenting: Thomas Bayes"
date: 2025-10-05 00:00:00-0000
description: "Some mathematicians spend their careers finding the right answers inside an already established framework. Others build conceptual tools so far ahead of their time that the world takes centuries to realize what they truly mean. Thomas Bayes decidedly belonged to the second kind."
categories: [presenting]
related_posts: false
---

<div class="portrait-duotone">
  <img src="{{ '/assets/img/thomas-bayes.png' | relative_url }}" alt="Portrait of Thomas Bayes" />
</div>
<p class="portrait-caption">The only known portrait that is probably of Bayes, from a 1936 book,<sup>1</sup> but it is doubtful whether the portrait is actually of him.<sup>2,3</sup></p>
<p class="portrait-caption" style="margin-top: -1rem;">
1. T. O'Donnell, <em>History of Life Insurance in Its Formative Years</em> (Chicago: American Conservation Co., 1936), p. 335 (caption "Rev. T. Bayes: Improver of the Columnar Method developed by Barrett.")<br />
2. <a href="http://www.york.ac.uk/depts/maths/histstat/bayespic.htm">Bayes's portrait</a>, The IMS Bulletin, vol. 17 (1988), no. 3, pp. 276 to 278.<br />
3. D. R. Bellhouse, <a href="https://projecteuclid.org/journals/statistical-science/volume-19/issue-1/The-Reverend-Thomas-Bayes-FRS--A-Biography-to-Celebrate/10.1214/088342304000000189.full">"The Reverend Thomas Bayes, FRS: A Biography to Celebrate the Tercentenary of His Birth"</a>, Statistical Science, 19(1), p. 3, 2004.
</p>

Some mathematicians spend their careers finding the right answers inside an already established framework. Others build conceptual tools so far ahead of their time that the world takes centuries to realize what they truly mean. **Thomas Bayes decidedly belonged to the second kind.**

Born around 1701 in Hertfordshire, England, and died in 1761 in Tunbridge Wells, Bayes was not an elite academic shut away in a university. He was a Presbyterian minister, an amateur philosopher, and a mathematician who published very little in his lifetime [1]. Yet his greatest legacy came from radically reorganizing how we understand uncertainty and how we learn from the world around us.

The work that puts his name in this article was not even published by him. It was discovered among his papers after his death and published in 1763 [2]. The central idea sounds almost like common sense when stated informally: our beliefs about the world should be updated mathematically every time we receive new evidence. The consequences of that simple idea, however, built modern artificial intelligence.

That became what we now call **Bayes' theorem**, and it changes a surprisingly basic question. Instead of asking how likely an event is given a system's parameters, we can ask what the system's parameters are given the event we just observed.

---

## The engine of intrigue: the life of a quiet minister

To understand Bayes' work, you have to understand the intellectual climate of his time. Unlike Markov, Bayes was not a furious polemicist. He was a quiet, deeply religious thinker. Yet he was immersed in one of the biggest philosophical battles of the eighteenth century: the debate over causality and miracles, driven by the skeptical philosopher David Hume [3].

Hume argued, in essence, that we cannot prove causes and effects are truly connected, and that believing in miracles was statistically irrational. Many believe Bayes, as a religious minister, developed his mathematical theory of probability to try to refute Hume. He wanted to show it was mathematically possible for humanity to rationally infer the existence of a "First Cause" (God) by observing the order of the universe, the evidence [3], [4].

**What drove him to study what he studied?** The need to give belief rigor. Bayes wanted a formula that could mathematically calculate how a rational mind should change its opinion upon receiving new empirical data. Remarkably, despite solving the mathematical problem, Bayes never published his essay. It was his friend, fellow minister Richard Price, who reviewed Bayes' notebooks after his death, recognized the brilliance of the finding, and presented it to the Royal Society in 1763 [2].

---

## The problem before Bayes

To understand what changed, it helps to recall what classical probability looked like in his time.

Before Bayes, probability theory was purely deductive, or forward looking. Jacob Bernoulli and Abraham de Moivre had mastered problems of this type: if you have an opaque urn with 3 red balls and 2 blue ones, what is the probability of drawing two reds in a row? That was easy to calculate. It was a probability that went from cause (the contents of the urn) to effect (the outcome of the draw) [4].

The problem is that in real life we almost never know the contents of the urn. We are trapped outside it. We see the effects and try to guess the causes. Bayes asked the inverse question, inductive probability: if I do not know what is in the urn, but I draw 3 red balls and 2 blue ones, what is the probability that the urn holds a majority of red balls? Bayes wanted to show how we can learn from experience to guess the hidden rules of the universe. And that required a mathematical way to update knowledge.

---

## Updating beliefs with evidence

Suppose you have a hypothesis about the world and then observe new evidence. Bayes' theorem states that your new belief should be a combination of your original belief and the weight of the new evidence:

$$P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}$$

where $A$ is your hypothesis, $B$ is the observed evidence, and $P$ is probability.

- $P(A)$ is the **prior**, what you believed before seeing the evidence.
- $P(B \mid A)$ is the **likelihood**, how probable this data is if your hypothesis were true.
- $P(A \mid B)$ is the **posterior**, your updated belief.

The important word here is not formula. It is update. We are asking how a logical mind should change its opinion in a mathematically perfect way.

**What this looks like in practice.** Imagine you take a test for a rare disease that affects 1% of the population. The test is 90% accurate. If you test positive, do you have a 90% chance of being sick? Human intuition screams yes. But Bayes says no: because the disease is so rare (your prior belief is low), a positive result on an imperfect test is probably a false positive. Applying his theorem, the real probability of being sick is only around 8%. Bayes showed that our intuition is terrible at handling uncertainty, but his mathematics is infallible.

---

## Subjectivity does not mean irrationality

This is where the theory set off a war that lasted two centuries.

Consider the concept of the prior, $P(A)$. To use Bayes' theorem, you have to start with an initial belief, even if it is an educated guess. Throughout the nineteenth and twentieth centuries, the rival statistical school, the frequentists, led by figures like Ronald Fisher, hated this. They argued that science had to be purely objective, and that introducing a "subjective" belief into a mathematical equation was heresy [3]. For a long time, Bayesianism was considered taboo.

But Bayes' theorem shows something profound: initial subjectivity does not matter in the long run. If two people start with completely different prior beliefs, one wildly optimistic, the other pessimistic, but both use Bayes' theorem to update their beliefs with the same ongoing evidence, their opinions will eventually converge toward the exact truth. The method purges subjectivity through the accumulation of data.

---

## The limits of the idea and the questions it left open

Bayes' theorem is mathematically flawless, but applying it to the real world was nearly impossible for more than 200 years.

Bayes' work left behind monumental questions that could only be resolved with the arrival of computers:

1. **Computational hell.** The denominator of the equation, $P(B)$, requires calculating the probability of the evidence under every possible hypothesis. With three hypotheses, that is easy. With thousands of variables, as in genetics or climate science, the equation requires integrals that are impossible to solve by hand. It was not until the invention of algorithms like MCMC (Markov Chain Monte Carlo) in the computing era that Bayes' theorem became practical [3].

2. **The origin of the prior.** How do you choose your initial belief if you know absolutely nothing? Philosophers and statisticians still debate "uninformative priors." If you assume everything is equally likely, the Principle of Indifference, are you not already introducing a bias?

3. **Human cognition.** Is the human brain secretly Bayesian? Modern cognitive science suggests our biological neural networks constantly update predictions about the world using an approximation of Bayes' theorem, the "predictive brain" theory [5].

---

## When the system learns from the world

If a formula lets you update predictions based on new evidence, its final destiny is not pure mathematics, but artificial intelligence.

During the Second World War, Alan Turing secretly used Bayesian reasoning to crack the Nazi Enigma machine, constantly updating the probabilities of the machine's configuration as German letters were intercepted [3].

Decades later, in the late 1990s, when email was flooded with junk, programmers built the "Naive Bayes" algorithm. It analyzed the words in a new email and calculated: given that this email contains the words "Viagra" and "Nigerian Prince," what is the probability that it is spam? Today, self-driving vehicles, recommendation algorithms, and generative artificial intelligence all depend deeply on Bayesian inference to navigate a world full of uncertainty and noise.

---

## In a nutshell: the gossip on Thomas Bayes

If we had to sum up this whole story informally:

Thomas Bayes was a super chill Presbyterian minister in the eighteenth century who liked thinking about numbers in his spare time. He invented the most important mathematical formula in the history of probability, probably because he wanted to logically prove the existence of God and shut up skeptics like David Hume. But because he was a perfectionist, or just very humble, he wrote the definitive answer in his notebook, stuck it in a drawer, and died without telling anyone.

Years later, his friend went to clean out his things, found the paper, said "hey, this is pretty interesting," and sent it off to be published. For the next 200 years, plenty of traditional statisticians hated his formula and called it unscientific. And yet today, that same note Bayes left in a drawer is the exact math behind your spam filter, the math Turing used to defeat the Nazis, and the foundational basis for how modern artificial intelligence learns from its mistakes. Not bad for an unpublished note.

---

## References

[1] D. R. Bellhouse, "The Reverend Thomas Bayes, FRS: A Biography to Celebrate the Tercentenary of His Birth," Statistical Science, vol. 19, no. 1, pp. 3 to 43, 2004.

[2] T. Bayes, "An Essay towards solving a Problem in the Doctrine of Chances," Philosophical Transactions of the Royal Society of London, vol. 53, pp. 370 to 418, 1763. (Presented by R. Price).

[3] S. B. McGrayne, The Theory That Would Not Die: How Bayes' Rule Cracked the Enigma Code, Hunted Down Russian Submarines, and Emerged Triumphant from Two Centuries of Controversy. New Haven, CT: Yale University Press, 2011.

[4] S. M. Stigler, "Thomas Bayes's Bayesian Inference," Journal of the Royal Statistical Society. Series A (General), vol. 145, no. 2, pp. 250 to 258, 1982.

[5] A. Clark, Surfing Uncertainty: Prediction, Action, and the Embodied Mind. Oxford, UK: Oxford University Press, 2016.

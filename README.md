# Numer.ai experiments

In this repository I will be publishing my research, experiments and iterative solutions to the [Numer.ai](https://numer.ai/) ML competition. This is just a learning exercise, I don't know how much I will last. Hopefully this repository will be of help for anyone wanting to get into Numer.ai, as one of the core principles of Numer.ai is to avoid reinventing the wheel.

## What is Numer.ai?

Numer.ai is a unique Machine Learning competition. It is also a unique Quantitative Analysis outsourcing company.

In Numer.ai people compete to create the best model for stock prediction and trading strategies. If your model is good, you get payed. However, Numer.ai differs from other Quant outsourcing companies in that it "encrypts" the data in a form perserving way while making it almost unrecognizable. Thanks to this, Numer.ai can release their highly privative data, avoid building a complex framework to host the models in and give maximum freedom to data scientists.

Using blockchain technologies and autioning strategies, they also extablish an economic system with the correct incentives to optimize distributed collaboration. The result is a "meta-model" as they call it, a weighted ensemble of all the best models. This is all explained in their [whitepaper](https://numer.ai/whitepaper.pdf).

Using such a homomorphic encryption has interesting consequences. On the one part, it completely removes any bias and need for domain knowledge. They claim that this is an advantage, as the Quant trade is aparently full of misinformed biases, but I'm skeptical as for the complete removal of domain knowledge.

For better of worse, the Numer.ai is a pure ML exercise. A by-the-book dataset of records with ~20 features and a binary classification task. Which is strange, as stock information is time-series data. I assume that they encode the time series context into the relatively low dimensional feature vector. This is very limiting, as it closes the door to modern deep models, leaving us playing with the good ol' RandomForest and SVN ensembles. A shame, but it is not like the competition ([Quantopian](https://www.quantopian.com/), [QuantConnect](https://www.quantconnect.com/)...) support for deep models either. Still an interesting challenge.

One final note to take into account, you own your model, mostly because you only upload the output, which is good. However, it's not like your model has any value outside of Numer.ai. If you wanted to get into proper Algorithmic Trading, look elswhere. Again, a pure ML abstract challenge, for better or worse.

## Goals

* I'm very familiar with the ML toolset and algorithms, but I haven't ever engaged in a classical pure ML task, I want to exercise those muscles.

* It's also the first time I engage in a explicit ML competition with leaderboards and all. I could try Kaggle, but I just chose Numer.ai, as good as any.

* I don't have any expectations, but I would be lying if the potential of getting payed didn't influence the decision.

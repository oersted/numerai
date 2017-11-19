# Iter 1 - 12/11/2017

Here we go. Let's see how I do.

I've been doing some research not to start from scratch. Now I have a fairly good idea of what is to be expected and, 
I have a plan of action.

## Ideas

* Baseline, that's number one. They already provide a baseline, so I'll make it into a notebook and play with it.

* From [this](https://medium.com/jim-fleming/notes-on-the-numerai-ml-competition-14e3d42c19f3) article I already have 
a rough idea of how the data looks like. I know that the features are uniform and some are highly correlated. I also 
know that, at surface level, there's not much more to know, the encryption is good. I may invest some energy into 
looking into the data at a later iteration, but this is enough for now.
  
* The encryption method is secret, but I know that this is usualy done with a deep autoencoder or GAN. Stock data is 
time series data, so I asume that that information is encoded into the low dimensional feature vector. All this means 
that the features are deep and abstract. People haven't had much success with deep NNs, but concatenating deeper 
features such as polynomial combinations and dimensionality reduction embeddings (PCA, t-SNE...) does help. Honestly, 
I don't know what this means, I guess I'll have to experiment.
  
* It's pure ML, clean binary classification. Forget about deep models, there's no use for RNNs or CNNs (unfortunately). 
RandomForests, SVNs, ensembles, automatic hyperparamenter optimization and feature engineering are the kings in this 
world. Numer.ai says that removing domain knowledge is ultimately beneficial. I'm not sure about that, but let's play 
with it. The data is secret and abstract, so automatic search will be the best strategy. Originality is a big barrier 
of entry in Numer.ai, so complex ensembles are probably the way to go. First step: try all the out-of-the-box stuff 
from sklearn that makes sense.
  
* I don't expect to get any good results in this iteration, I just want to do general research on single models from 
sklearn. I'll play with hyperparameter tuning, feature engineering and ensembles in a later iteration.

## Findings

* I made the baseline pretty easily. Based on it, I made a series of utility functions to make training other models 
much easier. Just the plumming. Other than that, I didn't learn too much from playing with the baseline.

* The sklearn cheat-sheet directed me to SGDClassifier, and I run with it, and I hit the wall. SGDClassifier contains
most of the main linear classifiers and it trains them using SGD, so loss functions with no analitical solutions
can also be trained. Most models I tried were slightly worse than the baseline, bummer.

    * Aparently only a few classifiers support probability estimation, so I couln't use the SVM loss for example, I was
    stuck with LogReg and Huber. Not that it matters too much, the difference between these loss functions would have 
    been marginal, the power of SVM comes when introducing kernels, not when sticking to a linear base. The out-of-the-box
    LogReg and Huber tests where almost identical (and slightly worse) as the baseline. Which makes sense, the baseline
    is standard LogReg.
    
    * Seeing as it is a binary classification problem, why not ignore the probability estimation, and just give a
    binary output? Clearly, not a good idea. This dataset is extremely hard to predict, looking at LogReg results
    they are all very close to 0.5, so high uncertainty. Which such high uncertainty, jumping to the extremes (binary)
    results in awful evaluations.
    
    * I stayed with linear models, but I did try doing kernel preprocessing to have an idea of how an SVM would perform.
    I tried the standard RBF kernel. Again, same thing, slightly worse than baseline.
    
    * I also tried adding polynomial features. Extremely RAM heavy, I could only add 2nd degree polynomials. Again, same
    thing.
    
    * I also dipped my toes in ensembles. I tried doing AdaBoost with LogReg. I also tried the default DecisionTree
    AdaBoost, nothing.
    
    * I didn't get clear learnings of what single classical models would perform best, as I had hoped. The only thing I
    learned is that, out of the box, they are all equally useless.
    
* Doing some more research on the internet, I found out that the incentives for both competitions are different. In the
general competition, the priority is to get a low logloss on the test set, so you can be in the top 100 that gets NMR.
However, in the staked competition, what matters most is to stay consistently above a random model (< -ln(0.5) logloss),
so people focus consistency rather than getting the highest accuracy possible. This is good to keep in mind, although
my current priority is to get NMR.

## Future work

* I'm never going to beat the originality condition on sigle models, no matter the hyperparameter tuning. So if I'm not
learning anything specific about what direction to take, why bother playing with these out-of-the-box models at all.
    
    * I've seen the use of complex feature selection. That could be enough variation to beat originality and (maybe)
    get decent results. I've seen people doing pre-clustering to then train different models on the clusters,
    adding all kinds of extra features (polynomial, PCA, t-SNE), doing feature selection by looking at the most
    chosen featues by DecisionTree ensembles. However, I don't have the time to do indepth feature engineering,
    it's not my strong suite anyways. I'd prefer to stick to the automatic side of things, I'd like to go deeper into
    AutoML.
    
    * Overall, I've seen that these simple models are unable to extract any meaninful signal. This may be fine, and 
    indented. The official help does say that the signal in the data is minimal, and top results are ~0.67, when the
    baseline is ~0.69 and so is random classification (-ln(0.5)). Maybe I should just go to the oposite side and
    start playing with NNs. This also ties into automatic feature engineering.

* It would be a good idea to compare the results to -ln(0.5) as well as the baseline.

# Week 1 - 12/11/1995

Here we go. Let's see how I do.

I've been doing some research not to start from scratch. Now I have a fairly good idea of what is to be expected and, I have a plan of action.

## Ideas

* Baseline, that's number one. They already provide a baseline, so I'll make it into a notebook and play with it.

* From [this](https://medium.com/jim-fleming/notes-on-the-numerai-ml-competition-14e3d42c19f3) article I already have a rough idea of how the data looks like.
  I know that the features are uniform and some are highly correlated. I also know that, at surface level, there's not much more to know, the encryption is good.
  I may invest some energy into looking into the data at a later iteration, but this is enough for now.
  
* The encryption method is secret, but I know that this is usualy done with a deep autoencoder or GAN. Stock data is time series data, so I asume that that information
  is encoded into the low dimensional feature vector. All this means that the features are deep and abstract. People haven't had much success with deep NNs, but concatenating
  deeper features such as polynomial combinations and dimensionality reduction embeddings (PCA, t-SNE...) does help. Honestly, I don't know what this means, I guess I'll have
  to experiment.
  
* It's pure ML, clean binary classification. Forget about deep models, there's no use for RNNs or CNNs (unfortunately). RandomForests, SVNs, ensembles, automatic hyperparamenter
  optimization and feature engineering are the kings in this world. Numer.ai says that removing domain knowledge is ultimately beneficial. I'm not sure about that, but let's
  play with it. The data is secret and abstract, so automatic search will be the best strategy. Originality is a big barrier of entry in Numer.ai, so complex ensembles
  are probably the way to go. First step: try all the out-of-the-box stuff from sklearn that makes sense.
  
* I don't expect to get any good results in this iteration, I just want to do general research on single models from sklearn.
  I'll play with hyperparameter tuning, feature engineering and ensembles in a later iteration.

## Findings
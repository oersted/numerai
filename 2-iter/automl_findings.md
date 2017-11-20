# AutoML findings

I've done a bit of research. [This](https://www.kdnuggets.com/2017/01/current-state-automated-machine-learning.html)
recent article by KDnuggets is the best source I've found, although not the only one I've used.

Here are the current "standard" tools I've found:

* [Auto-sklearn](http://automl.github.io/auto-sklearn/stable/#). A drop-in replacement aparently. Based on 
state-of-the-art Bayesian Optimization, it has won a few competitions. Seems perfect for my needs.

* [TPot](https://github.com/rhiever/tpot) is based on genetic algorithms. It's popular in Numer.ai too, I've seen it
in the forums. A nice plus of TPot is that it produces a script with the most succesful model that can be then
tweaked manually.

* [hyperopt](http://hyperopt.github.io/hyperopt/). It is a more general, well known, distributed search toolkit.
It says that it implements Random Search and Tree of Parzen Estimators. It also says that it was designed to 
integrate Bayesian Optimization but it is not yet implemented, bummer. I guess it's focus is the "distributed"
part. There is a separate non-documented [repository](https://github.com/hyperopt/hyperopt-gpsmbo) that seems to 
implement Bayesian Optimization. There's also [integration with sklearn](http://hyperopt.github.io/hyperopt-sklearn/),
similar idea to Auto-sklearn, but without Bayesian Optimization.

* [Spearmint](https://github.com/HIPS/Spearmint). Similar to hyperopt in that it enphasizes distributed general
optimization, but this one is specialized in Bayesian optimization.

* [RoBO](http://www.ml4aad.org/automl/robo/) is also in a similar vain.

* [skopt](https://scikit-optimize.github.io/) is a more obscure library also for Bayesian general black-box function
optimization.

* There's also ml-as-a-service stuff from AWS, Azure and Google Cloud. I tried the AWS one a bit with no success,
but it was a bit rushed, I could try again. There is also H2O.ai, which is dedicated to this. Google has an AutoML
project for training deep model architectures, but they haven't released it yet.

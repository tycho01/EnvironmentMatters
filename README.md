# EnvironmentMatters
Set of codes to show that, for evolutionary computing, the environment shapes the path of evolution.

Showcase 1 for polynomial functions:

Imagine that your robots are polynomial functions of a finite power and the genes are the respective coefficients, kept between `-1` and `1` for simplicity's sake.
An example of such robot is `y = 0.5*x^4 + 0.3*x^3 -0.1*x^2+0*x-0.8`.

The fit function is the highest possible value of `Y`. If `n = 5`, our max possible value of `Y` is `5`. The environment is the value of `X` that we plug in the function to get the `Y`.
This piece of code shows that if we chose our environments to be the constant functions `x = 1` and `x = -1` our robots will optimize their coefficients to yield the highest values of `Y`.

Ideally, we would get robots of the environment `x = 1` to be `y = 1*x^4+1*x^3+1*x^2+1*x+1` and robots of the environment `x = -1` to be `y = 1*x^4-1*x^3+1*x^2-1*x+1`.
More importantly, the robots of the environment `x = 1` will yield a poor performance in the negative environment and the opposite also holds.

Therefore the hypothesis 0 must be true, the environment matters.

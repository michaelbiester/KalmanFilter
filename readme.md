# Learning about Kalman-Filter

I wanted to learn about Kalman filtering and in the process of doing so, I have tried several resources with limited / mixed success.

## 1st attempt

The highly recommende article
`An Introduction to the Kalman Filter`; authors: Greg Welch, Gary Bishop

did not work for me due to missing background information.

---

**2'nd  attempt**

I then found the higly readable article

`An Elementary Introduction to Kalman Filtering`  , authors: Yan Pei, Donald S. Fussel, Swarnendu Biswas, Keshav Pingali

I tried to understand most parts of the article and reproduced some content from this article in a number of Ipython notebooks:

`kalman_introduction_part1.ipynb`

**keywords**

weighted addition of random variable -> mean and variance of these addtions.

random vectors, covariance matrix, weighted addition of random vectors with weighting factors as matrices -> covariance matrix of weighted addition 

weighted addition of two scalar random variables and determining the weights which minimise the variance of the addition. Repeating the process with > 2 random variables.

finally some numerical examples demonstrate these concepts.

---

`kalman_introduction_part2.ipynb`

**keywords**

vector estimates, adding two vectors weihted each by a matrix, compute covariance matrix and determine weighting matrices which minimise the quadratic norm (basically the sum of the variances (diagonal elements of the covariance matrix is minimised))
A review of matrix derivatives

---

`kalman_introduction_part3.ipynb`

**keywords**

state update or state evolution equation and covariance of the state update vector as a function of the covariance matrix of the estimated state vector. 

---

## 2'nd attempt

Here I tried to understand the article:

`A Kalman Filtering Tutorial for Undergraduate Students`; authors: Matthew B. Rhudy, Roger A. Salguero, Keaton Holappa

International Journal of Computer Science & Engineering Survey Vol.8, No.1 February 2017

and reproduced some content from this article in a Ipython notebook:

`kalman_simulation.ipynb`

the notebook only covers part of the material presented in the article. The derivation of Kalman gain is missing .

The notebook reproduces a simulation from the article. 

---

## 3'rd attempt

source:

`Kalman and Bayesian Filters in Python author`: Roger R Labbe Jr

adapted from chapter 2 of `Kalman_and_Bayesian_Filters_in_Python.pdf`


Worked through the first chapters to learn about Kalman-Filtering.

Read about the g-h or alpha-beta filter and prepared a Ipyhon notebook. 

`tracking_filter.ipynb`

Although the book is very readable it also very light  on math. 

So I looked for another resource which covers the derivation of the Kalman filter while not leaving out the underlying mathematical aspects (linear algebra, statistics, estimation theory, linearisation).

---
---

## 4'th attempt

I recently found a very readable account on the Kalman filter.

https://www.kalmanfilter.net

and bought the book `Kalman Filter from Ground Up`; author Alex Becker. The book covers topics not available on the web-site.

It seems that the book does not omit the underlying mathematical concepts as many other resources do. I started from chapter 3 and documented my learning progress with a series of Ipython notebooks. For each chapter there are one or more notebooks. 

### chapter 3

`kalmanfilter_chapter_3.ipynb`

**keywords**

recursive averaging of measured value, alpha-beta or g-h filter, numerical examples

### chapter 4

`kalmanfilter_chapter_4.ipynb`

**keywords**

one-dimensional Kalman filter, recursive state estimation, minimising the variance 

### chapter 5

`kalmanfilter_chapter_5.ipynb`

**keywords**

how process noise affects the estimation process

some numerical experiments 

### chapter 6

`kalmanfilter_chapter_6.ipynb`

**keywords**

covariance, numerical example of uncorrelated and correlated data, multivariate normal distribution

A separate notebook `multivariate_gaussian_1.ipynb` deals with some details of the properties of the multivariate normal distribution.

### chapter 7

The content of chapter 7 of the book `Kalman Filter from Ground Up` is explored by a series of notebook (instead of putting everything into a single notebook)

`kalmanfilter_chapter_7_covariance.ipynb`

a detailed discussion of the covariance matrix in 2D

a review of properties of the multivariate normal distribution

`kalmanfilter_chapter_7_1.ipynb`

The Kalman filter is extended to multiple dimensions and some mathematics of expectations / variances are reviewed.

### chapter 8

`kalmanfilter_chapter_8.ipynb`

the equations for the Kalman filtering process:

1) state extraplation equation

2) covariance extrapolation equation

3) process noise

4) measurement equation

5) state update equation with Kalman gain as a weighting factor

### chapter 9

`kalmanfilter_chapter_9.ipynb`

a numerical example of a vehicle moving in 2 dimensions with external forces.

1) motion equations -> state extrapolation equation

2) covariance extrapolation equation

3) process noise

4) measurement equation

5) state update equation

### chapter 10 & 11

`kalmanfilter_chapter_11.ipynb`

mathematical background 

1) square root of a matrix

2) Cholesky decomposition of a symmetric positve definite matrix

numerical example using `numpy`.

### chapter 12

`kalmanfilter_chapter_12.ipynb`

Linear system vs. non-linear systems and nonlinear measurements.

### chapter 13

In preparation to chapter 13 (extended Kalman filter) I had to review some math about linearisation of one dimensional and multi dimensional function. While the book provides a good overview I found it insufficient to get a more thourough knowledge. 

`kalmanfilter_linearisation_methods.ipynb` 

is a notebook which covers the mathematics of linearisation techniques. It makes heavy use of these resources:

https://ocw.mit.edu/courses/18-02-multivariable-calculus-fall-2007/pages/readings/supp_notes/

https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/82620/eth-8432-01.pdf

<ins>Topics</ins>

1) linear approximation in one dimension

2) linear approximation in two dimensions

3) linear approximation in > 2 dimensions; numerical example of 3D linear approximation

4) propagation of uncertainty (how mean and covariance of the input affect the mean and covariance of the output)

    a) one input -> one output 

    b) many inputs -> one output

    c) many inputs -> many outputs 

Currently there a 3 notebooks on the extended Kalman filter:

`kalmanfilter_chapter_13_ekf_1.ipynb`

derives and summarises the equations required for the extended Kalman filter.

`kalmanfilter_chapter_13_ekf_2.ipynb`

reproduces an example of the book; includes a simulation

`kalmanfilter_chapter_13_ekf_3.ipynb`

reproduces another example from chapter 13 of the book.

---

### chapter 14

In the book chapter 14 covers the `unscented`-Kalman filter.

To book presents the `unscented`-Kalman filter in a `cookbook`-style. Topics like `sigma points` are just stated without much background information.

As preperational steps I had to review the concept of `statistical linear regression` which is explained in the annex of the book.

`statistical_linear_regression.ipynb` is a notebook on `statistical linear regression` . It basically follows the steps decribed in annex F of the book.

I would have liked are more detailed discussion on the concept of `sigma-points` than what is provided by the book.

I found the article 

`a general method for approximating nonlinear transformations for probability distributions`, authors: Simon Julier, Jeffrey Uhlmann

helpful. 

The notebook 

`unscented_transform_and_sigma_points.ipynb`

reviews parts of the article and provides a numerical example which computes the covariance matrix after nonlinear transformation using different approaches:

1) simulation

2) using sigma points

3) using linearisation techniques 

**Todo**

1) prepare a notebook which summarises main facts of the `uncented Kalman filter`.

2) a notebook with some numerical examples















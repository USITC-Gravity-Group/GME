## Introduction to GME

The Gravity Modeling Environment (GME) package is a collection of tools written in Python to be used for gravity trade analysis.  The package consists of tools to aid in the fast, flexible, and robust estimation of gravity models using modern, best practices.  Future updates to the package will include tools for the simulation of general equilibrium gravity models and the preparation of data for estimation.

The GME package offers several distinct advantages over alternative software choices for conducting gravity analysis.  First, the package is written in Python, a flexible, powerful, and free programming language that can be readily used on a wide variety of computers with no cost. Second, unlike more general statistical software, which must cater to a broad number of needs, the GME package has been specifically designed to perform gravity analysis well. Third, because the tools are implemented in Python, users have access to an enormous and growing collection of third-party tools to incorporate into and expand their work.

Visit the [USITC gravity portal](https://gravity.usitc.gov) for more information about the Gravity Modeling Environment, which includes the GME package and a collection of data.

## Package Overview

In the current release, the GME package consists of three key components: the EstimationData object, the EstimationModel object, and the estimate() function. The EstimationData object houses the data to be used for estimation as well as information about the data and a set of tools to facilitate descriptive analysis of the data. The EstimationModel object is used to set up the specification for the estimation of the model and store the eventual results and diagnostic information. Finally, the function estimate() runs a Poisson Pseudo-Maximum Likelihood (PPML) estimation according to the specification established in the EstimationModel.

## Latest Version: 1.3
To see what is new in version 1.3, see [v1.3 updates](../updates)






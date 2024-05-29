## MATH 341: Python Assignment 5

This assignment/tutorial will walk you through real-world usage of the Central Limit Theorem, hypothesis testing, 
and confidence intervals using the tools and datasets that we've worked with all quarter.

This assignment will also introduce the scipy stats library:
<https://docs.scipy.org/doc/scipy/index.html>

First, make sure that the relevant python libraries are installed in your environment.

### Preliminaries
Briefly browse the scipy documentation linked above to see all of the methods, tests, and tools that it contains.  
In particular look at all the probability distributions (discrete and continuous) and tests in this library.  
Much more than we've covered in class, but - take heart - if you understand what we've covered you'll be able to 
learn any of these if you need them.

Run the `create_nhl_data`, and  `create_mnist_dataframe` method provided to download and do some processing on the 
datasets you will use for this assignment.  

### Problem 1: 
The method `clt_visualizer` is a Python version of <https://onlinestatbook.com/stat_sim/sampling_dist/>.

Create methods called `problem_one_continuous` and `problem_one_discrete` that use this template function 
to demonstrate the Central Limit theorem for two other distributions available which are available in scipy.  Feel free to leave
various variables like axis limits and titles hard-coded or make them dynamic.

* As the names suggest, one must be a discrete distribution and one a continuous distribution. 
* Both distributions should be ones we haven't discussed in class.
* Look up the theoretical means of your distributions and compare them to what you see on your histograms.
* A discrete distribution should be plotted with a bar chart, not a (line)plot.  


### Note for problems 2 and 3:
Many `scipy.stats` distributions have a method called `interval` to compute confidence intervals instead 
of finding $\overline{x}$ and $z_{\alpha/2}$ by hand.  
See <https://www.geeksforgeeks.org/how-to-calculate-confidence-intervals-in-python/> for example.

### Problem 2:
Calculate the mean and 90% CI for the `CENTER_SUM` for a particular label taken as the argument to the method.  
Comment on whether your results for the digits zero, six, and eight make sense given the boxplots 
that are displayed when you run the `create_mnist_dataframe` code.

Can you use the normal distribution or should you use Student's t-distribution here?


### Problem 3:
Calculate the mean and $\alpha$ confidence interval for the number of assists per game of an NHL defenseman on some particular 
team.  The dataframe, team abbreviation and CI level ($\alpha$) should all be inputs to the method. 

Can you use the normal distribution or should you use Student's t-distribution here?

Is there something funny about your results?  Look at Chicago or Washington.  Comment, please.

### Problem 4: 
In the 2022-23 season, defensemen for the Colorado Avalanche scored 60 goals, while the Washington Capitals'
defensemen scored only 19 goals.  Turn the snippet of code provided to write a function that tests
the hypothesis that one particular team's defensemen are better than the other D-corps in the league 
(i.e. it's not just random chance).  

Specifically, the null hypothesis is that each team's defensemen are equally offensively skilled.

### Problem 5: 
Run the `create_mnist_dataframe` method, which returns the flattened MNIST handwritten digits dataframe, augmented
with one of the features you investigated in the last lab, `CENTER_SUM`, indicating the brightness of the center of
the image.

The code snippet above `problem_five()` in `main` uses a ttest to determine whether or not are drawn 
from the same distribution.  Use that ttest code to loop over all unique pairs of digits, print the output of 
the `stats.ttest` method and an additional statement if the p-value is less than 0.05.
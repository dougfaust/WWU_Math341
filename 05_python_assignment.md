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
The method called `problem_one` recreates the CLT visualizer we used in class using a pretty boring distribution.  
Change the distribution to something interesting and highly skewed (e.g. Weibull with a parameter value >2).  
Add the ability for the method to take two arguments `n`, the number of samples used to 
calculate the mean, and `repetitions` the number of times a mean (over `n` samples) is calculated for the histogram.

### Problem 2:
Calculate the mean and 90% CI for the `CENTER_SUM` for a particular label.  Comment on whether your results 
for the digits zero, six, and eight make sense given the boxplots that are displayed when 
you run the `create_mnist_dataframe` code.

Can you use the normal distribution or should you use Student's t-distribution here?


### Problem 3:
Calculate the mean and 90% CI for the number of assists per game of an NHL defenseman on some particular 
team.  

Can you use the normal distribution or should you use Student's t-distribution here?

Is there something funny about your results?  Look at Chicago or Washington.

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
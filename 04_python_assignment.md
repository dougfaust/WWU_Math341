## MATH 341: Python Assignment 4

This assignment will involve visualizing the data and summary statistics from datasets.

First, make sure that pandas, numpy, matplotlib, and scikit-learn are installed in your environment.

### Preliminaries
Run the `download_clean_mnist` method provided to download and do some processing on the MNIST handwritten letter 
dataset.  Verify that the download worked by running the `plot_sample_digits` method.  Notice how the 8x8 image 
is being treated in the dataset (a flattened array) and in the plot method (reshaped into a grid of pixels).

### Problem 1: 
Write a method that adds some new columns to the DataFrame that add each of the following features:
* The total sum of the pixel brightness for each letter. Name this column `TOTAL_INK`.
* The sum of the pixel values for the four center pixels. Name this column `CENTER_SUM`.

### Problem 2:
You want to test some ideas that you should be able to distinguish letters in the MNIST handwritten letter dataset using 
the features you created above.  (e.g. `8` should be more likely to have a bright central pixel than `0` and `9` uses 
more ink than `1`.)

The first step in doing this is exploratory data analysis.  Write a method that shows a plot of the side-by-side
box plots of the values of one of these features.  Comment in your code about whether you think any of these 
features is promising.  

Uncomment and understand the code in the .py file for the most elegant way to do this visualization.

### Problem 3:
The iris dataset is also available through scikit learn.  Write a method similar to `download_clean_mnist` which returns 
a DataFrame of the entire iris dataset.  Your method should do the two following data-wrangling tasks: 

* Include the species type (the `target`) in the DataFrame.
* Change the units on the numerical column from `cm` -> `mm` and cast them to integers

### Problem 4: 
Quartiles divide the data into four even pieces.  Deciles divide the data into ten even pieces.  Generally, the 
term `quantiles` refers to any such partition of data into even pieces.  Write a method that prints out the 
probability that an iris belongs to each of the three species, given that its sepal length is in the top `80%` that is 
quintile value $q >= 0.8$.


Hint: Any basic statistical quantity should have a Pandas method for computing it.

### Problem 5: 
Suppose, for whatever reason, your job demands a stem-and-leaf plot for some data.  
In the python ecosystem, there are two generally-used ways to accomplish a task that 
one does not wish to build from the ground up:

1) Find a code snippet using libraries you're already using (Pandas) on StackExchange.
2) Find a Python library* that does what you want.  
*Very obscure libraries should be installed in a virtual environment as a best security and stability practice.

Write a function that displays (or saves to image file) a stem-and-leaf plot using either method listed above.  
Test your function on 50 random samples from a column of the iris dataset, converted from `cm` to `mm` and cast to integers.

### Problem 6:
Pick a modern visualization method like `bubble charts` or `violin plots` from one of the popular python visualization
libraries like `seaborn`, `bokeh`, or `plotly` and create any interesting chart from either of the datasets that 
we used above.  Make sure your plot has clear axes, title, and legend.
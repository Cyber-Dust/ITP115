#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Welcome to your HW1 notebook :)


# First, let's bring in our required modules (renaming them as they come in):

# In[3]:


print("Hello INF250!")


# Your turn - create cells below, to read in the Fortune500 csv file, and compute summary for Revenues.
# 
# Since you have the notebook .pynb file and the dataset files in the same dir, you can simply specify the filename of the dataset, otherwise you'd specify the entire path to the filename. 
# 
# You would use the Pandas .read_csv() command, to read the csv file. The result (output) of read_csv() is a DataFrame object: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html 
# 
# Once you have a dataframe (a rectangular frame of data), you can perform operations on it.
# 
# a. create a cell, to read in fortune500.csv
# 
# b. create a cell below, to rename the 'Revenues (in millions)' column to just 'Revenues'. Hint: use .rename(), with a columns={old:new} argument.
# 
# c. create another cell, to summarize the 'Revenues' column (print out the mean, std deviation, etc). Hint: in a dataframe, each column can be accessed as a dictionary key.

# In[38]:


import pandas as pd

pd.read_csv("fortune500.csv")


# In[23]:


company.columns


company.rename(columns = {'Revenue (in millions)':'Revenue'}, inplace = True)


# In[24]:


company[["Revenue"]].describe()


# Next, let's work on the 'iris' dataset.
# 
# As before, first open the dataset, create a dataframe. Note that unlike the fortune500 dataset, this one does NOT have column names listed at the top (so you need to make sure you read all the rows as data, including the first row) - you need to 'manually' specify these column names: 'Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Class'.
# 
# 'Describe' the dataset, then print out the top 5 lines. 
# 
# Use matplotlib to plot a histogram for each of the 4 columns - use 20 as the number of 'bins' for each column. Here's matplotlib: https://matplotlib.org/ and within it, the .hist() histogram command: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html (you only need to specify a column name and num_bins, as a bare minimum).
# 

# In[37]:


import pandas as pd

iris = pd.read_csv("irisdataset.csv")

print(iris)


# In[18]:


# Append .columns to dataframe, insert column names using [,x,y,z]
iris.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width', 'Class']

print(iris)


# In[13]:


# .describe() creates basic statisitical overview. Append describe() to dataframe.
iris.describe()


# In[16]:


# .head() allows us to display top 5 lines (0-4). Default hist() is 5.
iris.head()


# In[25]:


# .hist() using 20 as the number of bins (bins=)
hist = iris.hist(bins=20)


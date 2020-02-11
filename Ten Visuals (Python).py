#-------------------------------------------------------------------------------
#Towards Data Science Dataset for TenVisualisations
#https://towardsdatascience.com/10-viz-every-ds-should-know-4e4118f26fc3
#-------------------------------------------------------------------------------
#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import re
#-------------------------------------------------------------------------------
#Set working directory 
print(os.getcwd())
os.chdir("C:\\Users\\KOMSUN\\Documents\\GitHub\\TenVisualisations\\Data Sources")
ThermoStat  = pd.read_csv("thermostat_rebates_by_zip_1000.csv")
#-------------------------------------------------------------------------------
#1. Histogram
#Plotting the thermostatic rebate (USD)
sns.set_style("darkgrid")
fig, ax = plt.subplots() #Put the whole graph in a "subplot" but will still give a normal graph #HACK
fig.set_size_inches(11.7,8.27)
plt.hist(ThermoStat["rebate-usd"],bins=15)
plt.title('Histogram of Thermostatic Rebates (USD)', fontsize = 20)
plt.xlabel('Rebate (USD)',fontsize = 14)
plt.ylabel('Frequency',fontsize = 14)
plt.show()
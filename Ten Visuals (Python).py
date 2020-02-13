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
#-------------------------------------------------------------------------------
#1. Histogram
#Plotting the thermostatic rebate (USD)
ThermoStat  = pd.read_csv("thermostat_rebates_by_zip_1000.csv")
sns.set_style("darkgrid")
fig, ax = plt.subplots() #Put the whole graph in a "subplot" but will still give a normal graph #HACK
fig.set_size_inches(11.7,8.27)
plt.hist(ThermoStat["rebate-usd"],bins=15)
plt.title('Histogram of Thermostatic Rebates (USD)', fontsize = 20)
plt.xlabel('Rebate (USD)',fontsize = 14)
plt.ylabel('Frequency',fontsize = 14)
plt.show()
#-------------------------------------------------------------------------------
#2. Bar/Pie Charts
Drugs = pd.read_csv("drugs_data.csv")
sns.set_style("darkgrid")
fig, ax = plt.subplots() #Put the whole graph in a "subplot" but will still give a normal graph #HACK
fig.set_size_inches(11.7,8.27)
#Bar Charts
sns.catplot(x="BP", kind="count", palette="spring", data=Drugs) #Create a count plot
plt.title("Drugs Data for Patients", fontsize = 16)
plt.xlabel("Patients' Blood Pressure Type",fontsize = 10)
plt.ylabel('Number of Patients',fontsize = 10)
plt.show()
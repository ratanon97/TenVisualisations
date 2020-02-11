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
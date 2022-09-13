#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

#importing files and setting variables

#SPARCS Data
sparcs = pd.read_csv('data-enrichment/Data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')

#neighborhood atlas data (using .txt file)
nbhood_atlas = pd.read_csv('data-enrichment/Data/US_2019_ADI_Census Block Group_v3.1.txt')


#creating columns
sparcs.columns
nbhood_atlas.columns

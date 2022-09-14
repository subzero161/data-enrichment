#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

#importing files and setting variables

#SPARCS Data
sparcs = pd.read_csv('data-enrichment/Data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv', low_memory=False)
# get a count of the number of rows and columns
sparcs.shape
## clean the data
# list columns
list(sparcs)
############## COLUMN NAMES ##############
# remove all special characters and whitespace ' ' from column names
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 
list(sparcs)
# change all column names to lowercase
sparcs.columns = sparcs.columns.str.lower()
# change all column names to upper case
sparcs.columns = sparcs.columns.str.upper()
# replace all whitespace in column names with an underscore
sparcs.columns = sparcs.columns.str.replace(' ', '_')


#neighborhood atlas data (using .txt file)
#updated with correct file fron 2015 with zipcode and not FIPS
nbhood_atlas = pd.read_csv('data-enrichment/Data/NY_2015_ADI_9 Digit Zip Code_v3.1.txt')
# get a count of the number of rows and columns
nbhood_atlas.shape
## clean the data
# list columns
list(nbhood_atlas)
############## COLUMN NAMES ##############
# remove all special characters and whitespace ' ' from column names
nbhood_atlas.columns = nbhood_atlas.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 
list(nbhood_atlas)
# change all column names to lowercase
nbhood_atlas.columns = nbhood_atlas.columns.str.lower()
# change all column names to upper case
nbhood_atlas.columns = nbhood_atlas.columns.str.upper()
# replace all whitespace in column names with an underscore
nbhood_atlas.columns = nbhood_atlas.columns.str.replace(' ', '_')

#Print function used to get indexes of data columns
#print(nbhood_atlas.columns, print(sparcs.columns))


###############################################################
### Data index was saved duue tp KeyError In pandas package ###
### KeyError still persisted ##################################
###############################################################
##Data indexes: atlas:(['UNNAMED_0', 'X', 'TYPE', 'ZIPID', 'FIPS_X', 'GISJOIN', 'FIPS_Y', 'ADI_NATRANK', 'ADI_STATERNK'], dtype='object')
###Data indexes: sparcs: (['HEALTH_SERVICE_AREA', 'HOSPITAL_COUNTY','OPERATING_CERTIFICATE_NUMBER', 'FACILITY_ID', 'FACILITY_NAME','AGE_GROUP', 'ZIP_CODE_3_DIGITS', 'GENDER', 
#'RACE', 'ETHNICITY','LENGTH_OF_STAY', 'TYPE_OF_ADMISSION', 'PATIENT_DISPOSITION','DISCHARGE_YEAR', 'CCS_DIAGNOSIS_CODE', 'CCS_DIAGNOSIS_DESCRIPTION',
#'CCS_PROCEDURE_CODE', 'CCS_PROCEDURE_DESCRIPTION', 'APR_DRG_CODE', 'APR_DRG_DESCRIPTION', 'APR_MDC_CODE', 'APR_MDC_DESCRIPTION',
#'APR_SEVERITY_OF_ILLNESS_CODE', 'APR_SEVERITY_OF_ILLNESS_DESCRIPTION', 'APR_RISK_OF_MORTALITY', 'APR_MEDICAL_SURGICAL_DESCRIPTION',
#'PAYMENT_TYPOLOGY_1', 'PAYMENT_TYPOLOGY_2', 'PAYMENT_TYPOLOGY_3', 'BIRTH_WEIGHT', 'ABORTION_EDIT_INDICATOR', 'EMERGENCY_DEPARTMENT_INDICATOR', 'TOTAL_CHARGES', 'TOTAL_COSTS'], dtype='object')



#Matching 3 digit zip data from sparcs to atlas
nbhood_atlas['ZIPID'] = nbhood_atlas['ZIPID'].str.slice(1,4)

#Making new variable
nbhood_atlas_new = nbhood_atlas[['TYPE','ZIPID','ADI_NATRANK', 'ADI_STATERNK']]
sparcs_new = sparcs[['HOSPITAL_COUNTY', 'ZIP_CODE_3_DIGITS','AGE_GROUP','ETHNICITY','LENGTH_OF_STAY']]


#renaming zipcode column on sparcs csv file
sparcs.rename(columns={'ZIP_CODE_3_DIGITS':'ZIPID'}, inplace=True)


merged_data_sparcs = nbhood_atlas_new.merge(nbhood_atlas_new, how='left', left_on='ZIPID', right_on='ZIP_CODE_3_DIGITS')
merged_sparcs = sparcs_new.merge(nbhood_atlas_new, sparcs_new, how='left', left_on='ZIPID', right_on='ZIP_CODE_3_DIGITS')

#Outputing files to csv
merged_sparcs.to_csv('data-enrichment/Data/merged data.csv')
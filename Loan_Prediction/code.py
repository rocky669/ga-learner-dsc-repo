# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status=data.Loan_Status.value_counts()
loan_status.plot(kind='bar',figsize=(10,6))
plt.title('Loan Status')

#Creating a new variable to store the value counts
property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()
graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density', label='Graduate')
plt.show()
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='NOt Graduate')
plt.show()
fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1,figsize=(5,15))
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_1.set_title('Applicant Income')
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_2.set_title('Coapplicant Income')
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
ax_3.set_title('Total Income')
plt.show()
#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column


#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots


#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title




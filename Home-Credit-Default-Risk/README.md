# Home Credit Default Risk



# 1. Business/Real-world Problem

**Default risk** is the risk that a lender takes on in the chance that a borrower will be unable to make the required payments on their debt obligation. Lenders and investors are exposed to default risk in virtually all forms of credit extensions. A higher level of default risk leads to a higher required return, and in turn, a higher interest rate.

**Source Link**: [Investopedia.com](Investopedia.com)



# 2. Business Objectives
Home Credit strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.

**Source Dataset**: [Kaggle: Home Creidt Default Risk](https://www.kaggle.com/c/home-credit-default-risk/overview)

# 3. Constraints
> Low latency
> High Accurate Model

# 4.  Data Overview

Overall there are 9 CSV files and the description as follows:

- **Application_{train|test}** - This is the main table, broken into two files for Train (with TARGET) and Test (without TARGET). Static data for all applications. One row represents one loan in our data sample.

- **Bureau** - All client's previous credits provided by other financial institutions that were reported to Credit Bureau (for clients who have a loan in our sample). For every loan in our sample, there are as many rows as number of credits the client had in Credit Bureau before the application date.

- **Bureau_balance** - Monthly balances of previous credits in Credit Bureau. This table has one row for each month of history of every previous credit reported to Credit Bureau – i.e the table has (#loans in sample * # of relative previous credits * # of months where we have some history observable for the previous credits) rows.

- **POS_CASH_balance** - Monthly balance snapshots of previous POS (point of sales) and cash loans that the applicant had with Home Credit. This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credits * # of months in which we have some history observable for the previous credits) rows.

- **Credit_card_balance** - Monthly balance snapshots of previous credit cards that the applicant has with Home Credit. This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample – i.e. the table has (#loans in sample * # of relative previous credit cards * # of months where we have some history observable for the previous credit card) rows.

- **Previous_application** - All previous applications for Home Credit loans of clients who have loans in our sample. There is one row for each previous application related to loans in our data sample.

- **Installments_payments** - Repayment history for the previously disbursed credits in Home Credit related to the loans in our sample. There is a) one row for every payment that was made plus b) one row each for missed payment. One row is equivalent to one payment of one installment OR one installment corresponding to one payment of one previous Home Credit credit related to loans in our sample.

 - **HomeCredit_columns_description** - This file contains descriptions for the columns in the various data files.
 - 
## The hierarchical relationship of the data:

![https://storage.googleapis.com/kaggle-media/competitions/home-credit/home_credit.png](https://storage.googleapis.com/kaggle-media/competitions/home-credit/home_credit.png)

# Performance Matrix

-  ROC curve as a metric to validate the results

# Type of Machine Learning Problem


It is a Classification problem, the goal is to train a model to learn how to predict the target variable.

- **0 - indicates the person will repay the loan**

- **1 - will have difficulty repaying the loan**

# Train and Test Dataset

Split the dataset randomly into three parts train, cross validation and test with 64%,16%, 20% of data respectively

# Exploratory Data Analysis

# Approach 

# Result Summary 


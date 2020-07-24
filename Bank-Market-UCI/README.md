# Bank Marketing UCI



# 1. Business/Real-world Problem

The increasingly vast number of marketing campaigns over time has reduced its effect on the general public. Furthermore, economical pressures and competition has led marketing managers to invest on directed campaigns with a strict and rigorous selection of contacts. Such direct campaigns can be enhanced through the use of Business Intelligence (BI) and Data Mining (DM) techniques.

**Source**:  [USING DATA MINING FOR BANK DIRECT MARKETING: AN APPLICATION OF THE CRISP-DM METHODOLOGY](https://pdfs.semanticscholar.org/1999/417377ec21ecf7f7f55af62975065f785fb2.pdf)

# 2. Business Objectives
The classification goal is to predict if the client will subscribe a term deposit (variable y).

# 3. Constraints
> Low latency
> High Accurate Model

# 4.  Data Overview

**Description**: The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (or not) subscribed.

**Input variables:**

-  **age**  (numeric)
- **job**  : type of job (categorical: "admin.","unknown","unemployed","management","housemaid","entrepreneur","student","blue-collar","self-employed","retired","technician","services")
- **marital**  : marital status (categorical: "married","divorced","single"; note: "divorced" means divorced or widowed)
- **education**  (categorical: "unknown","secondary","primary","tertiary")
- **default**: has credit in default? (binary: "yes","no")
-  **balance**: average yearly balance, in euros (numeric)
- **housing**: has housing loan? (binary: "yes","no")
- **loan**: has personal loan? (binary: "yes","no")
-  **contact**: contact communication type (categorical: "unknown","telephone","cellular")
-  **day**: last contact day of the month (numeric)
-  **month**: last contact month of year (categorical: "jan", "feb", "mar", ..., "nov", "dec")
-  **duration**: last contact duration, in seconds (numeric)
-  **campaign**: number of contacts performed during this campaign and for this client (numeric, includes last contact)
-  **pdays**: number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted)
-  **previous**: number of contacts performed before this campaign and for this client (numeric)
- **poutcome**: outcome of the previous marketing campaign (categorical: "unknown","other","failure","success")
-  **y**  - has the client subscribed a term deposit? (binary: "yes","no")

**Source** - [https://www.kaggle.com/c/bank-marketing-uci](https://www.kaggle.com/c/bank-marketing-uci)


# Performance Matrix

-  Precision - Recall - F1 Score
-  Confusion Matrix
-  Accuracy

# Machine Learning Objective and Constraints

**Objective**: Predict the probability value of each data-point belonging to two class

**Constraints:**  Class probabilities are needed, Low latency constraints

# Train and Test Dataset

Split the dataset randomly into two groups train and test with 80-20% rule

# Exploratory Data Analysis

# Approach 

# Result Summary 


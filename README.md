
# Term Deposit Prediction

## Background

Term deposit is one of the major source of income for banks. It is a mean of invesment held by financial institution. where the client's money is invested with an agreement for rate of interest over fixed amount of time, also known as term. The marketing strategies from the bank to sell and promote term deposits are vaaried from email marketing, advertisements, telephonic marketing, and digital marketing.

One of the most effective marketing to reach out to customers is the campaign through telephhonic marketing but one of the down side is that it requires huge invesment. Large call centers are contracted to execute these  marketing campaigns, thus it is critical to able to identify customers that are likely to have the potential to subscribe term deposits via call. In this project, the data science team aim to assist the marketing on predicting customer's potential to subscribe to term deposit through applying artificial neural network method.


## About the  Dataset


The data is related to direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe to a term deposit (variable y).

Features in this dataset include:

| Column | Description |
| --- | --- |
| `age` | Age of the client |
| `job` | Client occupations |
| `marital` | Marital Status ("married","divorced","single"; note: "divorced" means divorced or widowed)|
| `education` | Customer's latest education |
| `default` | Has credit in default? (binary: "yes","no") |
| `balance` | Average yearly balance, in Euros |
| `housing` | Does the customer have housing loan? (binary: "yes","no") |
| `loan` | Does the customer have personal loan? (binary: "yes","no") |
| `contact` | Types of communcation means to customers (categorical: "unknown","telephone","cellular") |
| `day` | Last contact day of the month (numeric) |
| `month` | Last contact month of year (categorical: "jan", "feb", "mar", …,) |
| `duration` | Last contact duration, in seconds (numeric) |
| `campaign` | Number of contacts performed during this campaign and for this client (numeric, includes last contact) |
| `pdays` | number of days that passed by after the client was last contacted from a previous campaign (numeric, -1 means client was not previously contacted) |
| `previous` | Number of contacts performed for the client before this campaign |
| `poutcome` | Outcome of the previous marketing campaign (categorical: "unknown","other","failure","success") |
| `y` | Has the client subscribed a term deposit? (binary: "yes","no") |


source: https://www.kaggle.com/datasets/prakharrathi25/banking-dataset-marketing-targets



## Conclusion

**The conclusions that can be drawn from the results of EDA and modeling using Artificial Neural Network (ANN) are**:


- The objective of this project is to predict client's potential to subscribe term deposit. The dataset is record of customers data from a previous marketing campaign. Analyzing customer's occupation, the outcome of previous campaign and means of communication can be useful on developing the marketing strategy. Addition to the EDA-based analysis, another approach with implementing Artifical Neural Network (ANN) can be very effective in improving the marketing strategy.


Based on the hypothesis, the data science team made a prediction model using Artificial Neural Network with the following results:


- The first sequential API model has peformed quite satisfactory with accuracy score 0.85 but tend to overfit, shown by the graphs above. Therefore, the team attempted to improve the model so that the accuracy score is increased and the model tend to be goodfit or the gap between training and validation from loss and accuracy graphs are closer. The result from the second model is that the accuracy score has made small improvement with 0.86 and the second model is still tend to overfit. With the satisfactory result of the accuracy scores, the model can be utilzed for telephone marketing on predicting which customer has the potential to convert or subscribe to term deposit.

## Model Deployment

Deployment Link : [HUGGING FACE - Term Deposit Prediction](https://huggingface.co/spaces/abisugiri/deposit_subscription_prediction)



## Author

- Abi Rahman Sugiri [@abisugiri](https://www.github.com/abisugiri)
- Batch: FTDS RMT 021


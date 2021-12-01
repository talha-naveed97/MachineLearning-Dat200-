# Background

You are a data scientist employed by the the Institute of Alien Diseases (IAD) to aid them in predicting a special heart condition in a life-form from a distant planet that arrived on Earth recently. Other researchers with IAD have collected information on a number of alien specimens, some of which are diagnosed with the heart condition, while others are healthy.

 

 

# Kaggle competition
You will participate in an In-Class Kaggle competition (only students enrolled in DAT200 course are allowed to participate), where you will compete with other fellow students on how well your model predicts the test data.

 

Link to our In-class competition on Kaggle:

DAT200-CA3-2021

https://www.kaggle.com/c/dat200-ca3-2021/ (Links to an external site.)

 

Here is the link to enter the competition (please don’t forward this link to others outside our DAT200-course, since we want to keep the competition In-class)

https://www.kaggle.com/t/c55757df758448beb4c30d697f3c2ba6 (Links to an external site.)

On the data-tab (https://www.kaggle.com/c/dat200-ca3-2021/data (Links to an external site.)) of the In-Class competition you will find three files:

training data
test data
sample submission
 

 

# Rules and context of the competition
Please find the suggested workflow in file ‘Workflow - CA3 - DAT200 - 2021.pdf (Links to an external site.)’. Use the workflow as a guide for how to train your classifiers, make predictions and upload the predictions to Kaggle. You'll find it in our DAT200 repository in folder CA3.

You learned only a handful of classifiers in DAT200 so far. Therefore, you have only these available for prediction. You can use the following classifiers implemented in scikit-learn:

Perceptron
Adaline
Logistic regression
Support vector classifier (SVC kernel=’linear’)
Support vector classifier (SVC kernel=’rbf’)
Decision trees
Random forests
K-Nearest Neighbours (K-NN)
You have not yet learned all details of cross validation and how to apply it in scikit-learn. Therefore, we will continue our practice of using many train_test_splits (of the training data) while searching of the best parameters of each classifier as we have done so far in the lectures.

You may try out training classifiers with different number of features in X, that is by removing features (feature selection) or making new features (feature engineering). You can also remove potential outliers if you identify some and if that improves your predictions.

You may collaborate with other students on the compulsory assignment, but you need to make your own submission to Kaggle and Canvas.

 

 

# Deliverables / submissions
To have the compulsory assignment approved you need to deliver the following:

Your name must appear on the leaderboard of our own Kaggle competition, which means that you must submit at least one prediction (link to leaderboard: https://www.kaggle.com/c/dat200-ca3-2021/leaderboard (Links to an external site.))

You need to beat the benchmark classification F1 score of 0.75. If you don't get above this benchmark, you will fail the compulsory assignment.

Submit (I) a Jupyter notebook; (II) PDF of Jupyter notebook; (III) Python code of your Jupyter notebook on Canvas with the code for training of your best classifier (please don’t submit code for all seven classifiers) and the computation of the prediction. Please make short comments throughout your notebook/code on what you are doing and how you choose the parameters of your final best classifier. Leave out everything that is not necessary, keep only what is needed (we will reject PDF's that are full of unnecessary stuff)!

If you use an alias in the Kaggle leaderboard, you must provide your Kaggle alias AND your real name at the beginning of your Jupyter notebook

Remember that you can get your compulsory assignment approved during the exercises, where you provide an oral discussion of your work.

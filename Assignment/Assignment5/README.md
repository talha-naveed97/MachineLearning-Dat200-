# Background
The mayor of Gotham City has hired you to investigate whether it is possible to predict the number of armed robberies in the different parts of Gotham and the surrounding areas. You have been handed a dataset containing several (124) demographical measurements for each part of the area.

Warning: Several of the measurements are done with sub-par tools, resulting in "missing" datapoints.

 

# Kaggle competition
You will participate in an In-Class Kaggle competition (only students enrolled in DAT200 course are allowed to participate), where you will compete with other fellow students on how well your model predicts the test data.

Link to our In-class competition on Kaggle: 

https://www.kaggle.com/c/dat200-ca5-2021/ (Links to an external site.) 

 

Here is the link to enter the competition (please don’t forward this link to others outside our DAT200-course, since we want to keep the competition In-class):

https://www.kaggle.com/t/aac43336951c4ea19ee0a25b5ef4eb34 (Links to an external site.) 

On the data website (https://www.kaggle.com/c/dat200-ca5-2021/data) of the In-Class competition you will find three files:

training data (Pickled object)
test data (Pickled object)
sample submission (.csv file)
These three files were replaced Monday 19. in the morning due to limits in the file formats and an error in the sample submission file. New files contain a "4" at the end. Please, re-download if your files do not contain the "4".


# Rules and context of the competition
The suggested workflow in file ‘DAT200_CA03_workflow.pdf’ is to a large extent still valid, though the training process and internal validation will be different.
A minimum of exploration of the data is expected, e.g. plotting, summaries, patterns of missing.
Keep in mind that the data set is somewhat high-dimensional, may have high multicollinearity and replicate measurements. You are free to use any regression method from DAT200. Minimum requirements are to use two pipelines, one containing a compression step and a regression method, one using a regression method directly on the pre-processed data. Write a short paragraph about the choice of methods and how this differs from analysing tall data, e.g. Boston house prices.
Tune hyperparameters as you have done previously. Report suitable performance evaluation metrics for the tuning in the process and for optimal parameter values of each regression method.
Apply the best performing model with optimal parameters on the test data and report your results from the Kaggle competition (including Kaggle user name).
You may collaborate with other students on the compulsory assignment, but you need to make your own submission to Kaggle and Canvas.
 

# Deliverables / submissions
To have the compulsory assignment approved you need to deliver the following:

Your name must appear on the leaderboard of our own Kaggle competition, which means that you must submit at least one prediction (link to leaderboard: https://www.kaggle.com/c/dat200-ca5-2021/leaderboard) (Links to an external site.)
You should make an effort to beat the benchmark classification accuracy score of 0.65839. If you don't get above this benchmark, more thorough explanations of strategies must be supplied.
Submit (I) a Jupyter notebook; (II) PDF of Jupyter notebook; (III) Python code of your Jupyter notebook on Canvas with the code for training of your best classifier and the computation of the prediction. Make short comments throughout your notebook/code on what you are doing and how you choose the parameters of your final best regression method. Leave out everything that is not necessary, keep only what is needed (including data exploration). We will reject PDF's that are full of unnecessary stuff!
If you use an alias in the Kaggle leaderboard, you must provide your Kaggle alias AND your real name at the beginning of your Jupyter notebook.

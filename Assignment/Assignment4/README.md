# Background
A group of scientists has asked for your help in identifying the habitability of planets far, far away using their new measurement tool - The Habitron 3000. Based on the measurements from the Habitron 3000 your job is to predict whether scanned planets are 1. Non-habitable, 2. Potentially habitable or 3. Very habitable.

 

# Kaggle competition
You will participate in an In-Class Kaggle competition (only students enrolled in the DAT200 course are allowed to participate), where you will compete with other fellow students on how well your model predicts the test data.

Link to our In-Class competition on Kaggle:

DAT200-CA4-2021

https://www.kaggle.com/c/dat200-ca4-2021/ (Links to an external site.) 

 

Here is the link to enter the competition (please don’t forward this link to others outside our DAT200-course, since we want to keep the competition In-Class)

https://www.kaggle.com/t/e1290aba7cc34b8fb8a6a167db4531ae (Links to an external site.) 

On the data-tab (https://www.kaggle.com/c/dat200-ca4-2021/data) of the In-Class competition you will find three files:

training data
test data
sample submission 
 

# Rules and context of the competition
The suggested workflow in file `DAT200_CA03_workflow.pdf` is to a large extent still valid, though the training process and internal validation will be different.
You have access to a range of classifiers, kernels and L1/L2-regularization in DAT200 so far. These can be combined in the way you want, but classifiers outside the curriculum are not allowed for the competition. A bit of exploration/visualisation before analysis is to be expected.
Classifier selection and hyperparameter tuning is the core of this exercise. Use the appropriate scikit-learn tools from Chapter 6 to automatically search for optimal parameter values. You will need to combine pre-processing (e.g. scaling, dimension reduction) with a classifier in at least two pipelines. One pipeline must include a classifier using a kernel (Chapter 5) and one pipeline must include a classifier using regularization. Optimize the corresponding hyperparameters.
Report suitable performance evaluation metrics for the tuning, including confusion matrices for optimal parameter values of each classifier.
Apply the best performing model with optimal parameters on the test data and report your results from the Kaggle competition (including Kaggle user name).
You may collaborate with other students on the compulsory assignment, but you need to make your own submission to Kaggle and Canvas.
A separate part of the compulsory is only to be included in the notebook, not to be submitted to Kaggle: Choose a suitable classifier to use on only the two-class problem distinguishing between the non-habitable and very habitable classes and produce a single ROC curve based on 5-fold cross-validation.

# Deliverables / submissions
To have the compulsory assignment approved you need to deliver the following:

Your name must appear on the leaderboard of our own Kaggle competition, which means that you must submit at least one prediction (link to leaderboard: https://www.kaggle.com/c/dat200-ca4-2021/leaderboard) (Links to an external site.)
You should make an effort to beat the benchmark classification accuracy score of 0.83433. If you don't get above this benchmark, more thorough explanations of strategies must be supplied.
Submit (I) a Jupyter notebook; (II) PDF of Jupyter notebook; (III) Python code of your Jupyter notebook on Canvas with the code for training of your best classifier and the computation of the prediction. Make short comments throughout your notebook/code on what you are doing and how you choose the parameters of your final best classifier. Leave out everything that is not necessary, keep only what is needed (we will reject PDF's that are full of unnecessary stuff)!
If you use an alias in the Kaggle leaderboard, you must provide your Kaggle alias AND your real name at the beginning of your Jupyter notebook

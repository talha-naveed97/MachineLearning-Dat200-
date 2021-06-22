# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:54:33 2019

@author: Talha Naveed
"""

#==============================================================================
# Import modules
#==============================================================================

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron,LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


#==============================================================================
# Load data and select features
#==============================================================================

data = pd.read_csv("train.csv")

print (data.target)
X = data.iloc[:, 1:9]
y = data.iloc[:,9]

#y = np.where(y, 1, -1)
# plt.figure(0)

# # Plot data for class 1
# plt.scatter(X[y == 1, 0],
#             X[y == 1, 1],
#             c='b', marker='x',
#             label='1')

# # Plot data for class -1
# plt.scatter(X[y == -1, 0],
#             X[y == -1, 1],
#             c='r',
#             marker='s',
#             label='-1')

# plt.xlim([-3, 3])
# plt.ylim([-3, 3])
# plt.legend(loc='best')
# plt.tight_layout()
# #plt.savefig('images/03_12.png', dpi=300)

# plt.scatter(X, y)


#==============================================================================
# Plot the data
#==============================================================================
plt.figure(0)

# Plot data for class 1
plt.scatter(data.target[y == 1, 0],
            data.target[y == 1, 1],
            c='b', marker='x',
            label='1')

# Plot data for class -1
plt.scatter(data.target[y == 0, 0],
            data.target[y == 0, 1],
            c='r',
            marker='s',
            label='-1')

plt.xlim([-3, 3])
plt.ylim([-3, 3])
plt.legend(loc='best')
plt.tight_layout()
#plt.savefig('images/03_12.png', dpi=300)
plt.show()



# Split data into training and test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=3, stratify=y)



#==============================================================================
# Scale features using StandardScaler class in scikit-learn 
#==============================================================================

# Initialise standard scaler and compute mean and STD from training data
sc = StandardScaler()
sc.fit(X_train)




# Transform (standardise) both X_train and X_test with mean and STD from
# training data
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)



# #==============================================================================
# # Train multiclass perceptron that is implemented in scikit-learn
# #==============================================================================

# # Initialise the model
# ppn = Perceptron(max_iter=40, eta0=0.1, random_state=1)
# ppn.fit(X_train_std, y_train)


# #==============================================================================
# # Train multiclass perceptron that is implemented in scikit-learn
# #==============================================================================

# # Initialise the model
# ppn = LogisticRegression(C=10, 
#                           random_state=1,
#                           solver='liblinear',
#                           multi_class='auto')
# ppn.fit(X_train_std, y_train)

# y_pred = ppn.predict(X_test_std)
# print('Misclassified samples: {0}'.format((y_test != y_pred).sum()))



# #==============================================================================
# # Compute performance metrics in a couple of ways
# #==============================================================================

# # Print accuracy computed from predictions on the test set
# print('Accuracy: {0:.2f}'.format(accuracy_score(y_test, y_pred)))


# # Print accuracy computed from predictions on the test set
# print('Accuracy: {0:.2f}'.format(ppn.score(X_test_std, y_test)))



﻿# Author: Miriam Heller <mheller8@gatech.edu>
# CS 7641, Spring 2016 GA Tech OMSCS
# Asssignment 1 - due February 7, 2016

# Comparison of 5 Supervised Learning Algorithms on 2 data sets

# Import digits dataset from sk-learns's built in 0-9 digit dataset
from sklearn.datasets import load_digits

# Import sk-learn supervised learning algorithms
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import tree
from sklearn import cross_validation
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix

# Import standard scientific Python packages
import numpy as np
import matplotlib.pyplot as plt
# get ipython().magic(u'matplotlib inline')

######################

digits = load_digits(n_class=10)


# In[98]:

kf = cross_validation.KFold(len(digits.target), n_folds=5)
print kf


# In[99]:

means = []
for neighs in range(1,11):
    accuracies = []
    for train_index, test_index in kf:
        neigh = KNeighborsClassifier(n_neighbors=neighs)
        X_train, X_test = digits.data[train_index], digits.data[test_index]
        y_train, y_test = digits.target[train_index], digits.target[test_index]
        neigh.fit(X_train, y_train) 
        trues, preds = [], []
        for i in range(len(X_test)):
            preds.append(neigh.predict(X_test[i]))
            trues.append(y_test[i])
        acc = accuracy_score(trues, preds)
#         print "Accuracy: ", acc, "Neighbors: ", neighs
        accuracies.append(acc)
    # accuracies has 5 values
    print "Mean Accuracy for ", neighs, " neighbors: ", np.mean(accuracies)
    means.append(np.mean(accuracies))
#means has 10 values
plt.scatter(range(1,11), means)
plt.xlabel('k-nearest neighbors')
plt.ylabel('Accuracy')
plt.savefig('knn.jpg')

# In[113]:

means = []
for c_value in range(-19,20,2):
    accuracies = []
    for train_index, test_index in kf:
        model = SVC(C=10**(c_value * -1))
        X_train, X_test = digits.data[train_index], digits.data[test_index]
        y_train, y_test = digits.target[train_index], digits.target[test_index]
        model.fit(X_train, y_train) 
        trues, preds = [], []
        for i in range(len(X_test)):
            preds.append(model.predict(X_test[i]))
            trues.append(y_test[i])
        acc = accuracy_score(trues, preds)
    #         print "Accuracy: ", acc, "Neighbors: ", neighs
        accuracies.append(acc)
    print "Mean Accuracy for C: ", 10**(c_value * -1), " Average:", np.mean(accuracies)
    means.append(np.mean(accuracies))

plt.scatter([10**(r * -1) for r in range(-19,20,2)], means)


# In[102]:

means = []
for depth in range(1,20,2):
    accuracies = []
    for train_index, test_index in kf:
        model = tree.DecisionTreeClassifier(max_depth=depth)
        X_train, X_test = digits.data[train_index], digits.data[test_index]
        y_train, y_test = digits.target[train_index], digits.target[test_index]
        model.fit(X_train, y_train) 
        trues, preds = [], []
        for i in range(len(X_train)):
            preds.append(model.predict(X_train[i]))
            trues.append(y_train[i])
        acc = accuracy_score(trues, preds)
    #         print "Accuracy: ", acc, "Neighbors: ", neighs
        accuracies.append(acc)
    print "Mean Accuracy for max depth: ", depth, " Average:", np.mean(accuracies)
    means.append(np.mean(accuracies))

plt.scatter(range(1,20,2), means)


# In[ ]:



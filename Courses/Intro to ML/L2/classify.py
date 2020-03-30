def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    
    ### My Code ### Testing block. Who is who
    print(type(pred))
    print(len(pred))
    print(pred[0:5])
    
    print(type(labels_test))
    print(len(labels_test))
    print(labels_test[0:5])
    
    ### My Code ### Compare element-by-element. If equal then 'labels_equal' counter +1
    labels_equal = 0
    labels_all = len(labels_test)
    
    for i in range(len(features_test)):
        if pred[i] == labels_test[i] : labels_equal += 1
    
    accuracy_ratio = labels_equal / labels_all   
    
    print("Equal Labels", labels_equal)
    print("All Labels Count", labels_all)
    print("Accuracy ratio", accuracy_ratio)
   
   

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    accuracy = 0
    return accuracy

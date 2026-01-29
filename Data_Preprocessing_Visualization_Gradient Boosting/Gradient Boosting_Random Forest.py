import Data_Preprocessing_Visualization
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

y = Data_Preprocessing_Visualization.df["HeartDisease"] # Dependent Variable.              

X = Data_Preprocessing_Visualization.df.iloc[:,:-1] # Independent Variables.

print(y, X)

ohe = OneHotEncoder(categories='auto', sparse_output = False).set_output(transform = "pandas") # One-Hot Encoding is applied to convert categorical features into binary variables, enabling the model to use categorical information effectively. 
                                                                                               # The output is a DataFrame containing dummy variables.

for col_X in range(len(X.columns)): # The following code collects all dummy variables into a list, converts them into a DataFrame, and appends them to the final dataset used by the model.  
    if col_X == 0:                  # Additionally, all variables of string type are removed, since the model cannot handle categorical string values directly.
        dummys = []
    if X.iloc[:,col_X].dtype == "string[python]":
        ohetransform = ohe.fit_transform(X[[X.iloc[:,col_X].name]])
        for col_ohetransform in range(len(ohetransform.columns)):
            dummys.append(ohetransform.iloc[:,col_ohetransform])


df = Data_Preprocessing_Visualization.pd.DataFrame(data = dummys) 

df = df.T

print(df)

for col_X in range(len(X.columns)):
    if col_X == 0:
        index_list = []
    if X.iloc[:,col_X].dtype == "string[python]":
        index_list.append(col_X)

X = X.drop(X.columns[index_list], axis = 1) 

X = X.join(df)

print(X)

########## Gradient Boosting Clasifier ##########

sum_accuracy_test = 0

count_test = 0

list_test = []

for r_s in range(1, 10): # The dataset is divided into 60% for training, 20% for validation, and 20% for testing.
    X_train, X_split, y_train, y_split = train_test_split(X, y, test_size = 0.4, stratify = y, random_state = r_s) # Different data splits are used, making the results more robust in terms of model accuracy and reliability.

    X_val , X_test, y_val, y_test = train_test_split(X_split, y_split, test_size = 0.5, stratify = y_split, random_state = r_s)

    if r_s == 1:
        print(X_train.shape, X_split.shape, y_train.shape, y_split.shape, X_val.shape, X_test.shape, y_val.shape, y_test.shape)

    l_r = 0.001

    sum_accuracy_val = 0

    count = 0

    best_learning_rate = 0

    best_learning_rate_accuracy = 0

    while l_r <= 0.10:
        G_B_C = GradientBoostingClassifier(n_estimators = 300, learning_rate = l_r) # A Gradient Boosting Classifier model is used with n_estimators = 300, which is within an acceptable range according to the literature.

        G_B_C.fit(X_train, y_train) # Initially, the training set is used to train the model and estimate its parameters.

        G_B_C_Predictions_val = G_B_C.predict(X_val) # The validation set is used to assess model fit while keeping the test set untouched for estimating performance on unseen data.

        accuracy = accuracy_score(y_val, G_B_C_Predictions_val)

        if best_learning_rate_accuracy <= accuracy:
            best_learning_rate_accuracy = accuracy
            best_learning_rate = l_r # The learning rate is tuned over a range of values, and the best-performing value on the validation set is applied to the test set.

        sum_accuracy_val += accuracy  

        count += 1
    
        l_r += 0.001
    
    G_B_C = GradientBoostingClassifier(n_estimators = 300, learning_rate = best_learning_rate)

    G_B_C.fit(X_train, y_train)

    G_B_C_Predictions_test = G_B_C.predict(X_test)

    accuracy_test = accuracy_score(y_test, G_B_C_Predictions_test)

    list_test.append(accuracy_test)

    sum_accuracy_test += accuracy_test

    count_test += 1

    print(f"Best_Learning_Rate = {round(best_learning_rate, 3)}",f"Best_Accuracy = {round(best_learning_rate_accuracy, 3)}",f"Average Accuracy = {round(sum_accuracy_val/count, 3)}",f"Accuracy_Test_Set = {round(accuracy_test,3)}", sep = "  ")

std_test_set = Data_Preprocessing_Visualization.np.std(list_test)

print(f"Average Accuracy Test Set = {round(sum_accuracy_test/count_test, 3)}",f"Standard Deviation Accuracy Test Set = {round(std_test_set, 3)}", sep = "  ")
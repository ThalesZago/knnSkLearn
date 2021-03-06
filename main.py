from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd

dataFrame = pd.read_csv('haberman.data',names = ['Age','year_P','N_nodes','Class'])

X = dataFrame.drop('Class', axis=1)
y = dataFrame['Class']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33, random_state=42)

neigh = KNeighborsClassifier(n_neighbors=3 )
neigh.fit(X_train, y_train)


y_pred = neigh.predict(X_test)

matrix = confusion_matrix(y_test, y_pred)

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

print(matrix)

print(f"tn, fp, fn, tp = {tn}, {fp}, {fn}, {tp} ")
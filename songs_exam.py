

import pandas as pd
from sklearn import tree 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
songs_data = pd.read_csv("https://stepik.org/media/attachments/course/4852/songs.csv")
X = songs_data.drop(['artist', 'year'], axis=1)
y = songs_data.artist
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=2)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
precision = precision_score(y_test, predictions, average='macro')

print(precision)
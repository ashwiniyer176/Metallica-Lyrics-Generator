from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
metric = metrics.accuracy_score
numberOfFolds = 3

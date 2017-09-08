from sklearn import tree

clf = tree.DecisionTreeClassifier()


X = [[95, 80, 44], [77, 70, 43], [60, 60, 38], [54, 54, 37], [66, 65, 40],
     [90, 90, 47], [85, 94, 39],
     [77, 70, 40], [59, 55, 37], [81, 95, 42], [81, 85, 83]]

Y = ['pass', 'fail', 'fail', 'fail', 'fail', 'pass', 'pass', 'fail',
     'fail', 'pass', 'pass']


clf = clf.fit(X, Y)

prediction1 = clf.predict([[60, 40, 43]])
prediction2 = clf.predict([[90, 75, 63]])
prediction3 = clf.predict([[83, 90, 83]])


print(prediction1)
print(prediction2)
print(prediction3)










import random
weeks=16
print (weeks, type (weeks))
classes=5
print (classes, type(classes))
tuition=6000
print (tuition, type(tuition))
cost_per_week= ((tuition/classes)/weeks)
print (cost_per_week, type(cost_per_week))
classes_per_week=2
print (classes_per_week, type (classes_per_week))
print ("Cost_per_week:", cost_per_week)
cost_per_class= (cost_per_week/classes_per_week)
print (cost_per_class, type (cost_per_class))
print ("Your cost per class is:", cost_per_class)
mylist= ("film", 2, 3.6, "sociology", 4, 5.5)
var= random.choice (mylist)
print ("Your random item is", var)
# created by ZHANG Jiachen
# simplest AI algorithm - linear regression
# goal equation is y = bx + a

# import
import matplotlib.pyplot as plt
from math import *

# specify known cases
x = [0, 1, 2, 3, 4, 5, 6]
y = [0.05, 0.08, 0.25, 0.5, 0.75, 0.92, 0.95]

# specify unknown cases
x_unknown = 2.5

# intermediate variables
n = len(x)                  # num. of known cases

converted_y = [0] * len(x)
for i in range( len(x) ):
    converted_y[i] = log( y[i] / ( 1-y[i] ) )

sum_x_y = 0
sum_x_square = 0
sum_x = 0
sum_y = 0

n = len(x)

for i in range(n):
    sum_x += x[i]
    sum_y += converted_y[i]
    sum_x_y += x[i] * converted_y[i]
    sum_x_square += x[i] ** 2

b = n * sum_x_y - sum_x * sum_y
b = b / (n * sum_x_square - sum_x ** 2)

a = sum_y / n - b * sum_x / n

print(a,b)

# convert to logistic curve
x_logistic = [0,1,2,3,4,5,6,7]
n = len(x_logistic)
y_logistic = [0] * n
for i in range(n):
    y_logistic[i] = exp(b*x_logistic[i]+a) / ( 1+exp(b*x_logistic[i]+a) )

# make predictions
y_prediction = exp( b * x_unknown + a) / ( 1 + exp( b * x_unknown + a ) )

#print('prediction for unknown case is %f' % y_prediction)

# plot results
plt.rc('font', size=15)          # controls default text sizes


plt.plot(x, y, 'r^', ms=20)
#plt.plot(x_combined, converted_y, 'b^')
#plt.plot(x_logistic, y_logistic, 'b-')
#plt.plot(x_unknown, y_prediction,'ks', ms=20)

plt.xlabel('average num. of hrs. for studying')
plt.ylabel('possibility of passing exam')

# titles
plt.title('Fig. 1: Known Cases')
#plt.title('Fig. 2: Logistic Regression (Training)')
#plt.title('Fig. 3: Prediction')

plt.axis([0,7,0,1])
plt.show()

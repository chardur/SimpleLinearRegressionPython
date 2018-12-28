import numpy as np
import matplotlib.pyplot as plt

# create arrays for the data points
X = []
Y = []

#read the csv file
csvReader = open('Salary_Data.csv')

#skips the header line
csvReader.readline()

for line in csvReader:
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

# change to numpy array
X = np.array(X)
Y = np.array(Y)

# view the data
plt.figure(1)
plt.scatter(X, Y)
plt.title("The data we're trying to model")

# use variables so that the sum, dot, and denominator is only calculated once
n = X.size
sumY = Y.sum()
sumX = X.sum()
sumXY = X.dot(Y)
sumX2 = X.dot(X)

denominator = (n * sumX2) - (sumX ** 2)
a = ((sumY * sumX2) - (sumX * sumXY)) / denominator
b = ((n * sumXY) - (sumX * sumY)) / denominator
print("the value of a is: ", a)
print("the value of b is: ", b)

# calculate predicted Y array
predictedY = a + b * X

# calculate the r-squared value
SSres = Y - predictedY
SStot = Y - Y.mean()
rSquared = 1 - (SSres.dot(SSres) / SStot.dot(SStot))
print("the value of R-squared is: ", rSquared)

# view the data and the line
plt.figure(2)
plt.scatter(X, Y)
plt.plot(X, predictedY)
plt.title("The data and our line")
plt.show()
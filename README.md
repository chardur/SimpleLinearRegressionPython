# Simple linear regression with Python, Numpy, Matplotlib
<br/>
Background info / Notes:  <br/>
Find a line that models the relationship between a dependent variable and an independent variable.  <br/>
<br/>
Equation: <br/> 
y = α + b*x  <br/>
<br/>
In English:<br/>
y is the dependent variable: what we are trying to predict<br/>
α is a constant: y at x = 0<br/>
b is a coefficient: slope of the line<br/>
x is the independent variable: what we think predicts y <br/> 
<br/>
Equation:  
<br/>
<br/>
&nbsp; &nbsp; &nbsp; &nbsp; [SUM(Y) * SUM(X^2)] - [SUM(X) * SUM(XY)] <br/>
α = ________________________________________ <br/>
      &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; n[SUM(X^2)] - [SUM(X)]^2<br/>
<br/>
<br/>
&nbsp; &nbsp; &nbsp; &nbsp; n[SUM(XY)] - [SUM(X) * SUM(Y)]<br/>
b = ___________________________________<br/>
        &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; n[SUM(X^2)] - [SUM(X)]^2<br/>
<br/>
SUM = Summation<br/>  
n = sample size
<br/>
<br/>
R-Squared:  
Tells us how good our prediction is, closer to 1 the better.  
Equation:  
<br/>
<br/>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SUM(Y - Yi)^2 <br/>
R^2 = 1 - _______________________________<br/>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; SUM(Y - Yavg)^2<br/>
<br/>
Y = the actual data point <br/> 
Yi = the predicted Y value  <br/>
Yavg = the average Y value  <br/>
<br/>
<br/>
Convert the equations to code (we can leverage the numpy dot function for SUM(XY) and SUM(X^2)):  <br/>
n = X.size  <br/>
sumY = Y.sum()  <br/>
sumX = X.sum()  <br/>
sumXY = X.dot(Y)  <br/>
sumX2 = X.dot(X)  <br/>
<br/>
denominator = (n * sumX2) – (sumX ** 2)  <br/>
a = ((sumY * sumX2) – (sumX * sumXY)) / denominator  <br/>
b = ((n * sumXY) – (sumX * sumY)) / denominator  <br/>
<br/>
SSres = Y – predictedY  <br/>
SStot = Y – Y.mean()  <br/>
rSquared = 1 – (SSres.dot(SSres) / SStot.dot(SStot))<br/>
<br/>
<p>
<img src="SLRpythonFig1.png" alt="image">
<br/>
<img src="SLRpythonFig2.png" alt="image">
</p>

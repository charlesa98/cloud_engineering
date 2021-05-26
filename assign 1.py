# problem 1
print(50+50)
print(100-10)
#problem 2
print('Hello World')
print('Hello World : 10')

#problem 3
print(30+6)
print(6+6+6+6+6+6)
print(6^6)
print(6**6)

#problem 4
p = 800000              #starting price
r = ((6/100)/12)        #interest rate
l = 103                 #the amount of months 
ppm = 0                 #price per month

t = 1 - pow(1+r, l)
ppm = r* pow(1 + r, l)* p/t
ppm = round(ppm)
print ('Total price per month is ', abs(ppm))

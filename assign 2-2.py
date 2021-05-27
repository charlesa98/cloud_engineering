#1. 
list = [1, 'word', float(1)]        #casted to float to make sure its a float
print(list)

#2.
list = [1, 1,[1,2]]
print(list[1])

#3.
lst = ['a','b','c']
print(lst[1:])

#4.
d = {"Mon": 1, "Tues": 2, "Wed": 3, "Thurs": 4, "Fri": 5}

#5.
D={'k1':[1,2,3]}
print(D['k1'][1])

#6. 
list = [1,[2,3]]
tuple(list)

#7.
s = "Mississippi"
print(str(set(s)))

#8.
s = s + "x"
print(s)
print(str(set(s)))

#9. 
s = [1,1,2,3]
print(str(set(s)))

#10.
l= ""
for x in range (2000, 3000):
    if(x%7 == 0 and x%5 != 0):      #if both divisible by 7 and not by 5
        l = l + str(x) +", "
print(l)

#11.
n = input("Number? ")
f = 1
for i in range(1, int(n)+1):
    f = f * i 
print(f)

#12
n = input("Number? ")
d = {}
for i in range(1, int(n)+1):
    d[i] = i*i
print(d)

#13
n = input("Comma seperated numbers? ")
l = n.split(",")
t = tuple(l)
print(l)
print(t)

#14.
class Myclass:
    def __init__(self):
        self.s=""

    def getString(self):
        self.s = input("Input a string ")

    def printString(self):
        print(self.s.upper())

strObj = Myclass()          # define a string object
strObj.getString()          # call the getString method
strObj.printString()        # call printString method
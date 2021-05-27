#pypi.org for some extra libraries 
#1. 
print("Hello World"[8])

#2. 
print("thinker"[2:5])
print("Hello"[0])

#3.
s = "Sammy"
print(s[2:])

#4. 
print("")
print("")
results =""
amount = input("How many lines do you want to check? ")
for x in range(int(amount)):                #make sure to cast this as an int
    s1 = input()
    s3 = s1[::-1]                           #set s3 = s1 but backwards
    s1 = s1.lower()                         #make them all lowercase
    s3 = s3.lower()
    compare = ([c for c in s1 if c.isalpha()] == [c for c in s3 if c.isalpha()])        #isalpha checks if all values in the string are letters with the for loop
    if(compare == True):                    #if the comparing results were true, add to the reult string
        results = results +"Y "
    else:                                   #else add N
        results = results +"N "     
print(results)

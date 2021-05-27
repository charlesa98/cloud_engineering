# Thres is a crowd
nl = ["Cindy", "Kyle", "Jack", "Sammantha"]

def crowded(l):
    if(len(l)>3):
        print("Too many people. Crowded")

o = crowded(nl)
del nl[2::]             #remove everyone after the second index
print(nl)

# Six is a mob
nl2 = ["Cindy", "Kyle", "Jack", "Sammantha", "Kevin", "Alyssa"]

def mob(l2):
    if(len(l2)>5):
        print("There is a mob in the room")
    elif(len(l2)>=3 and len(l2)<= 5):
        print("This room is crowded")
    elif(len(l2)>=1 and len(l2)<= 2):
        print("This room is not crowded")
    else:
        print("This room is empty")

o2 = mob(nl2)
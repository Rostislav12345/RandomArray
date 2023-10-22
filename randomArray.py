import random
arr = []
addatt= 1
while addatt == 1:
    for i in range(9):
   
        rand = random.randint(1,20)
    
        if rand not in arr :
            arr.append(rand)
        else:
            addatt += 1

temp1 = addatt
addatt = 0
for i in range(temp1):
    
    rand = random.randint(1,20)
    
    if rand not in arr :
        arr.append(rand)
 
    else:
        addatt += 1
print(arr)
print(addatt)
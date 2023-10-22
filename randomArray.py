import random
arr = []
addatt= 0
while addatt == 0:
    for i in range(10):
   
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
print(temp1)

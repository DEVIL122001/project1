for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()
    
   
# "#" pattern
print("\n------------------------------------")
for i in range(4):
     for j in range(4):
         print("#",end="")
     print()
print("\n----------------------------------")

for i in range(4):
    for j in range(i):
        print("#",end="")
    print()
print("\n-----------------------------------------")    
# for equilaterlar triangle 
n=30
for i in range(1,11):
    print(' '*n,end="")#repeat space for n times 
    print('* '*(i))# repeat star for i times
    n-=1
    
    
n=30
for i in range(1,11):
    print(' '*n,end="")#repeat space for n times 
    print('* '*(i))# repeat star for i times
    n+=1

print("\n------------------------------------------------")


for i in range(5):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("\n-------------------------------------------")
for i in range(5,0,-1):
    for j in range(i):
        print(i,end="")
    print()
    
    
    
for i in range(5):
    for j in range(i):
        print("    *",end="")
    print()
for i in range(3,0,-1):
    for j in range(i):
        print("    *",end="")
    print()
    
    

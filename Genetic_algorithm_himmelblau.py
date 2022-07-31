# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:54:32 2022

@author: Paras
"""
import random
import numpy as np

#Himmelblau function
#Constraints: 0<=x1,x2<=6
def f(x1,x2):
    return (x1**2+x2-11)**2 + (x1+x2**2-7)**2
#Population size    
n = 20
#String length
sl = 10
#Accuracy = (xu-xl)/(2**q-1)
acc = 0.006
#Chromosome length
cl = 20





#Reproduction starts
#Generating 20 random strings
x1x2 = [["" for i in range(2)] for j in range(20)]
for i in range(20):
    for j in range(2):
        temp = str(bin(random.randrange(0, 1024)))[2:].zfill(10)
        x1x2[i][j] = temp
oldx1x2 = list(map(list, x1x2))

#Modifying x1x2        
for i in range(20):
    for j in range(2):
        t = x1x2[i][j]
        x1x2[i][j] = round((0.005865)*(int(t,2)),3)
                
        
#Calculating f(x)        
fx = [0 for i in range(20)]
for i in range(20):
    a,b = x1x2[i]
    fx[i] = round(f(a,b),3)

    
#Calculating F(x)    
Fx = [0 for i in range(20)]
for i in range(20):
    Fx[i] = 1/(1+fx[i])





    
#Finding expected count A    
avg = sum(Fx)/20  
A = [0 for i in range(20)]
for i in range(20):
    A[i] = Fx[i]/avg


    
#Finding probability of selection B        
B = [0 for i in range(20)]
for i in range(20):
    B[i] = A[i]/20



#Finding cumulative probability C        
C = [0 for i in range(20)]
C[0] = B[0]
for i in range(1,20):
    C[i] = C[i-1]+B[i]


    
#Generating random numbers between 0 and 1        
D = np.random.rand(20)



#Picking strings for the mating pool    
selected = []
for i in range(20):
    val = D[i]
    j = 0
    while j<20:
        if val<C[j]:
            break
        j+=1
    
    selected.append(j)

newx1x2 = [["" for i in range(2)] for j in range(20)]
for i in range(20):
    newx1x2[i] = oldx1x2[selected[i]]


x1x2 = newx1x2
#Reproduction ends







#Crossover starts
  
#Deciding whether crossover should be performed or not    
cross = []
for _ in range(10):
    cross.append(random.randint(0, 1))



#Deciding the location of crossover
location = []
for _ in range(10):
    location.append(random.randint(1,20))  


#Performing crossover
#Calculating fitness of strings after reproduction
newx1x2 = list(map(list, x1x2))
for i in range(20):
    for j in range(2):
        if type(newx1x2[i][j])==type("01"):
            newx1x2[i][j] = round((0.005865)*(int(newx1x2[i][j],2)),3)
        


#Calculating f(x)        
fx = [0 for i in range(20)]
for i in range(20):
    a,b = newx1x2[i]
    fx[i] = round(f(a,b),3)
    
#Calculating F(x)    
Fx = [0 for i in range(20)]
for i in range(20):
    Fx[i] = 1/(1+fx[i])

   
newcombined = [["" for i in range(2)] for j in range(20)]
for i in range(0,20,2):
    if cross[i//2]==1:
        combined1 = x1x2[i][0]+x1x2[i][1]
        start1 = combined1[:location[i//2]]
        end1 = combined1[location[i//2]:]
        combined2 = x1x2[i+1][0]+x1x2[i+1][1]
        start2 = combined2[:location[i//2]]
        end2 = combined2[location[i//2]:]
        
        new1 = start1+end2
        new2 = start2+end1
        
        newcombined[i] = [new1[:10],new1[10:]]
        newcombined[i+1] = [new2[:10],new2[10:]]
        
    else:
        newcombined[i] = x1x2[i]
        newcombined[i+1] = x1x2[i+1]

x1x2 = newcombined
#Crossover completed
#Mutation starts

for i in range(20):
    temp = x1x2[i][0]+x1x2[i][1]
    for j in range(20):
        num = random.random()
        if num<0.05:
            temp = temp[:j]+"0"+temp[j+1:] if temp[j]=="1" else temp[:j]+"1"+temp[j+1:]
    
    x1x2[i] = [temp[:10],temp[10:]]

#Mutation completed
oldx1x2 = list(map(list,x1x2))

final = list(map(list,oldx1x2))
for i in range(20):
    for j in range(2):
        t = final[i][j]
        final[i][j] = round((0.005865)*(int(t,2)),3)
                
                
fx = [0 for i in range(20)]
for i in range(20):
    a,b = final[i]
    fx[i] = round(f(a,b),3)

        
Fx = [0 for i in range(20)]
for i in range(20):
    Fx[i] = 1/(1+fx[i])

index = Fx.index(max(Fx))
eliteS = oldx1x2[Fx.index(max(Fx))]
eliteFx = max(Fx)
print(eliteFx)



#Generations start
for generation in range(2,75):       
    #Modifying x1x2        
    for i in range(20):
        for j in range(2):
            t = x1x2[i][j]
            x1x2[i][j] = round((0.005865)*(int(t,2)),3)
                    
            
    #Calculating f(x)        
    fx = [0 for i in range(20)]
    for i in range(20):
        a,b = x1x2[i]
        fx[i] = round(f(a,b),3)
    
        
    #Calculating F(x)    
    Fx = [0 for i in range(20)]
    for i in range(20):
        Fx[i] = 1/(1+fx[i])
    
    
    
    
    
        
    #Finding expected count A    
    avg = sum(Fx)/20 
    elite = oldx1x2[Fx.index(max(Fx))] 
    A = [0 for i in range(20)]
    for i in range(20):
        A[i] = Fx[i]/avg
    
    
        
    #Finding probability of selection B        
    B = [0 for i in range(20)]
    for i in range(20):
        B[i] = A[i]/20
    
    
    
    #Finding cumulative probability C        
    C = [0 for i in range(20)]
    C[0] = B[0]
    for i in range(1,20):
        C[i] = C[i-1]+B[i]
    
    
        
    #Generating random numbers between 0 and 1        
    D = np.random.rand(20)
    
    
    
    #Picking strings for the mating pool    
    selected = []
    for i in range(20):
        val = D[i]
        j = 0
        while j<20:
            if val<C[j]:
                break
            j+=1
        
        selected.append(j)
    
    newx1x2 = [["" for i in range(2)] for j in range(20)]
    for i in range(20):
        newx1x2[i] = oldx1x2[selected[i]]
    
    
    x1x2 = newx1x2
    #Reproduction ends
    
    
    
    
    
    
    
    #Crossover starts
      
    #Deciding whether crossover should be performed or not    
    cross = []
    for _ in range(10):
        cross.append(random.randint(0, 1))
    
    
    
    #Deciding the location of crossover
    location = []
    for _ in range(10):
        location.append(random.randint(1,20))  
    
    
    #Performing crossover
    #Calculating fitness of strings after reproduction
    newx1x2 = list(map(list, x1x2))
    for i in range(20):
        for j in range(2):
            if type(newx1x2[i][j])==type("01"):
                newx1x2[i][j] = round((0.005865)*(int(newx1x2[i][j],2)),3)
            
    
    
    #Calculating f(x)        
    fx = [0 for i in range(20)]
    for i in range(20):
        a,b = newx1x2[i]
        fx[i] = round(f(a,b),3)
        
    #Calculating F(x)    
    Fx = [0 for i in range(20)]
    for i in range(20):
        Fx[i] = 1/(1+fx[i])
    
   
    newcombined = [["" for i in range(2)] for j in range(20)]
    for i in range(0,20,2):
        if cross[i//2]==1:
            combined1 = x1x2[i][0]+x1x2[i][1]
            start1 = combined1[:location[i//2]]
            end1 = combined1[location[i//2]:]
            combined2 = x1x2[i+1][0]+x1x2[i+1][1]
            start2 = combined2[:location[i//2]]
            end2 = combined2[location[i//2]:]
            
            new1 = start1+end2
            new2 = start2+end1
            
            newcombined[i] = [new1[:10],new1[10:]]
            newcombined[i+1] = [new2[:10],new2[10:]]
            
        else:
            newcombined[i] = x1x2[i]
            newcombined[i+1] = x1x2[i+1]
    
    x1x2 = newcombined
    #Crossover completed
    #Mutation starts
    
    for i in range(20):
        temp = x1x2[i][0]+x1x2[i][1]
        for j in range(20):
            num = random.random()
            if num<0.05:
                temp = temp[:j]+"0"+temp[j+1:] if temp[j]=="1" else temp[:j]+"1"+temp[j+1:]
        
        x1x2[i] = [temp[:10],temp[10:]]
    
    #Mutation completed
    oldx1x2 = list(map(list,x1x2))
    
    #Checking for the fittest individual
    final = list(map(list,oldx1x2))
    for i in range(20):
        for j in range(2):
            t = final[i][j]
            final[i][j] = round((0.005865)*(int(t,2)),3)
                    
                    
    fx = [0 for i in range(20)]
    for i in range(20):
        a,b = final[i]
        fx[i] = round(f(a,b),3)
    
            
    Fx = [0 for i in range(20)]
    for i in range(20):
        Fx[i] = 1/(1+fx[i])
    
    index = Fx.index(max(Fx))
    if eliteFx>max(Fx):
        oldx1x2[index] = eliteS
    else:
        eliteS = oldx1x2[Fx.index(max(Fx))]
        eliteFx = max(Fx)
        
    print(eliteFx)
    
print(eliteS)
x1 = round((0.005865)*(int(eliteS[0],2)),3)
x2 = round((0.005865)*(int(eliteS[1],2)),3)

print(x1,x2)




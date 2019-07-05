s=int(input())  
L=[]
if(s>0):
  for i in range(1,s+1,2):
    if(s%i==0):  
      L.append(i)  
print(*L)

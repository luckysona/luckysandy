s=int(input())  
L=[]
if(s>0):
  for i in range(2,s+1):
    if(s%i==0):  
      L.append(i)  
print(*L)

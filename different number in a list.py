s=int(input())  
s1=list(map(int,input().split()))  
l1=[]
l2=[]
for i in s1:
  if(i%2==0):
    l1.append(i)
  else:
    l2.append(i)
if(len(l1)==1):
  print(*l1)
else:
  print(*l2)

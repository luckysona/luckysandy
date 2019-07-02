a,s=input().split() 
a=int(a)  
s=int(s)
s1=list(map(int,input().split()))
if(s>0):
  for i in range(s-1):
    a=min(s1)
    s1.remove(a)  
print(min(s1))

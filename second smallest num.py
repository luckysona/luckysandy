s=int(input())  
s1=list(map(int,input().split()))
if(s>0):
  a=min(s1)
  s1.remove(a)  
print(min(s1))

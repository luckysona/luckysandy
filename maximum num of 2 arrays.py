a1,a2=input().split()
a1=int(a1)
a2=int(a2)
s1=list(map(int,input().split()))   
s2=list(map(int,input().split())) 
L=[] 
for i in s1:
  j=max(s1)  
  for i in s2:
    k=max(s2)
L.append(j)
L.append(k)
print(*L)

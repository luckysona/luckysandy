s1,s2=map(int,input().split())  
s1=int(s1)  
s2=int(s2)
count=0
for i in range(1,101):
  if i*i >= s1 and i*i <= s2:

    count=count+1
print(count)

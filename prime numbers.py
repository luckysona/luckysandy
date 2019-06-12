N,K=map(int,input().split())
h=list() 
for i in range(N,K+1):
  count=0
  for j in range(1,i+1):
      if(i%j==0):
         count+=1
  if(count==2):
        h.append(i) 
print(len(h))

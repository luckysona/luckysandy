h1,h2=map(str,input().split())
count=0
for h in range(len(h1)):
  if(h1[h]!=h2[h]):
      count+=1 
if(count==1):
  print("yes")
else:
  print("no") 

s1=int(input())  
s2=list(map(int,input().split()))
for i in range(0,len(s2)-1):
  if(s2[i]>s2[i+1]):
    print(s2[i],end=" ")
  else:
    print(s2[i+1],end=" ")

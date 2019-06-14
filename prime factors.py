k=[]
s1,s2=input().split()
a=int(s1)
b=int(s2)
for i in range(1,a+1):
  if((a%i==0)and(b%i==0)):
    k.append(i)
k.sort(reverse=True)
print(k[0])

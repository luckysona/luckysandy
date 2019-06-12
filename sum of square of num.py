t=int(input()) 
f=g=0
while(t!=0):
  g=t%10
  f=f+g**2
  t=t//10
print(f)

d1,d2=map(str,input().split())
d=0
for i in range(0,len(d1)):
    for j in range(0,len(d2)):
        if d1[i]==d2[j]:
            d+=1
if d>=2:
    print("yes")
else:
    print("no")

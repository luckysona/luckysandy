s=int(input())
count=0
l=[]
for k in range(s):
    l.append(input())
for k in range(s):
    if sorted(l[k])==sorted('kabali'):
        count=count+1
print(count)        

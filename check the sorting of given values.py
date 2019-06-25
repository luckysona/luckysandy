s1=int(input())
s2=list(map(int,input().split()))
a=sorted(s2)
if s2==a:
    print("yes")
else:
    print("no")

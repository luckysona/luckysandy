s1=int(input())
s2=list(map(int,input().split()))
s=s2
s2.sort()
if s2==s:
    print("yes")
else:
    print("no")

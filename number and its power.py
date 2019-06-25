num,pow=list(map(int,input().split()))
while num>1:
    num = num/pow
if num ==1:
    print("yes")
else:
    print("no")

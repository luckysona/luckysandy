num=int(input())
n=1
while(n<=num):
    c=0
    if(num%n==0):
        k=1
        while(k<=n):
            if(n%k==0):
                c=c+1
            k=k+1
        if(c==2):
            print(n,end=' ')
    n=n+1

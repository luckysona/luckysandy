N,K= map(int,input().split())
K= K%N
s1 = list(map(int,input().split()))
s2 = s1[-K:] + s1[:-K]
print(*s2)

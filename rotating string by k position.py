s1,s2=input().split()
s2=int(s2)
for i in range(s2):
    s1 = s1[-1] + s1[:-1]
print(s1)

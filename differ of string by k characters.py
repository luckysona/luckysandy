s1,s2,s3 = list(map(str,input().split()))
s3 = int(s3)
s = 0
for i in range(len(s1)):
  if s1[i] != s2[i]:
    s += 1
if s == s3:
  print("yes")
else:
  print("no")

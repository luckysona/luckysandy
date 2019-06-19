s=input() 
m=''  
L=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
for i in s:
  for j in range(0,len(L)):
    if (i==L[j]):
        m=m+L[(j+3)%26]
    elif i==L[j].lower():
		    m=m+L[(j+3)%26].lower() 
print(m)

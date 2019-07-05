s1=input().split() 
s2=input().split()  
s3=input().split()  
if(s1[0]==s2[0]==s3[0] or s1[1]==s2[1]==s3[1] or (s1[0]==s1[1] and s2[0]==s2[1] and s3[0]==s3[1])):
        print("yes")  
else:
        print("no")

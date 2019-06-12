i=int(input()) 
j=list(map(int,input().split()))
list_set = set(j) 
unique_list = (list(list_set))  
for x in unique_list:
  if (j.count(x)==1): 
    print(x)

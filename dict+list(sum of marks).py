dict = {'amit':[82,39,59,82,91], 'rohit':[82,85,79,88,90], 'ravi': [82,99,79,80,91]}

sum=0
for key, value in dict.items():
    for i in value:
        sum=sum+i
    dict[key]=sum
 
    
for key, value in dict.items():
    print('Student Name - Total Marks')
    for i in key:
        print(i,end='')
    print(" -",dict[key])    
    print()
    
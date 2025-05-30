
n = int(input("Enter Number : "))
count =0

for i in range(2,n//2):
    if(n%i==0):
        count +=1

if(count>0):
    print("Not Prime")
else:
    print("Prime")
    
    
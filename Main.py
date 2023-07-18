print("enter number")
num1 = int (input("enter number"))
primeOrNot = str
for i in range(2,num1-1):
    if num1%i==0:
        primeOrNot = 'not prime'
        break
        
else:
        primeOrNot = 'prime'
    
print(primeOrNot)
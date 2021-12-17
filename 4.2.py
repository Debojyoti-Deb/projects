num=int(input("Enter a 5 digit number :"))
sum=0
while (num!=0) :
    digit=num % 10
    sum=sum * 10 + digit
    num = num//10
print("The reversed number is :",sum)
if(num==sum) :
    print("They are same")
else :
    print("They are not same")
    

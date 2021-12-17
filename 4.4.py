print("To display the fibonacci series upto 50")
first=0
second=1
print(first,second,end=" ")
for i in range(0,8) :
    third=first + second
    first=second
    second=third
    print(third ,sep=",",end=" ")
    i=i+1

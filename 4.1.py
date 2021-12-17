print("Numbers which are divisible by 7 but are not a multiple of 5 are :")
for x in range(2000,2100) :
    if(x%7 == 0) and ( x%5 != 0) :
        print(x,sep=',',end=" ")

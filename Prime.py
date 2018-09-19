
number_1 = int(input("Enter number:"))

if number_1 > 1:
    for ind in range(2,number_1):
        if(number_1%ind) == 0:
            print(number_1, "is not a prime number")
            break   
    else:
        print(number_1,"is a prime number")
            
else:
    print(number_1, "is not a prime number")
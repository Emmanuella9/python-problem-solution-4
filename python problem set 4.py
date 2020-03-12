#Check if a number is prime or not

num = int(input("Enter a number:"))

#Prime numbers are always greater than 1
if num > 1:
    for j in range(2, (num//2)+1):
        if (num % j) == 0:
            print(num,"is not a prime number")
            
            break
        else:
            print(num, "is a prime number")

#if number is less than or equal to 1 or it is not prime
else:
    print(num, "is not a prime number")



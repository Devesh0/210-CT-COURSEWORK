def isPrime(num,div):
    if (div == 1):
        return True
    else:
        if (num % div ==0):
            return False
        else:
            return isPrime(num ,div-1)
        
n = int(input("Enter a number greater then 2: "))
print(isPrime(n,n//2))

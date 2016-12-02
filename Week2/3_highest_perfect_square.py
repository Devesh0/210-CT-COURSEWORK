def perfect_square(number):
    n = int(number)
    for x in range(1,n):
        if n < x**2 :
            n = (x-1)**2 #get to the lower number then x
            return(n)
        elif n == x**2:
            return(n)

print(perfect_square(input("Enter the number: ")))

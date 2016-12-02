def trailing_zeroes(n):
    
    count = 0
    while n >= 5:
        n = (n//5) # factors of n that are divisible to 5
        count += n
    return ("No. of trailing zeroes are: "+ str(count))

print(trailing_zeroes(int(input("Enter the number: "))))


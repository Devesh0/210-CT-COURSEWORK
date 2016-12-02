ISPRIME(num,div)
    if div = 1 // BASE CASE
        return TRUE
    
    if num (mod) div = 0
        return TRUE
        
    return ISPRIME(num,div-1)

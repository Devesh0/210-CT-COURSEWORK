PERFECT_SQUARE(number)
    n <- integer(number)
    for x <- 1 to n
        if n < x ** 2
            n <- (x-1)**2 // get to the lower number then x
            return n
    elif n = x ** 2
        return n

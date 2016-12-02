PERFECT_SQUARE(number)
    n <- integer(number)
    for x <- 1 to n
        if n < x mult x
            n <- (x-1)mult (x-1) // get to the lower number then x
            return n
    elif n = x mult x
        return n

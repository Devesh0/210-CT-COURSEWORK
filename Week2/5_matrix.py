##BIG-O : O(N^3)

M1 <- Matrix1 of order n  
M2 <- Matrix2 of order n

ADD_MATRIX(M1,M2)
    for i <- 1 to length[M1]    // Length of rows of M1
        for j <- 1 to length[M2[0]]   // Length of column of M2 
            M3 <- [M1[i][j] + M2[i][j]]
    RETURN M3

SUB_MATRIX(M1,M2)
    for i <- 1 to length[M1]
        for j <- 1 to length[M2[0]]
            M3 <- [M1[i][j] + M2[i][j]]
    RETURN M3

MULT_MATRIX(M1,M2)
    for i <- 1 to length[M1]
        for j <- 1 to length[M2[0]]
            M3[i][j] <- 0
            for k <- 1 to length[M2] //Length of rows of M2
                M3[i][j]<- M3[i][j] + M1[i][k]*M2[k][j]
    RETURN M3

MULT_MATRIX_COF(M,2)
    for i <- 1 to length[M]
        for j <- 1 to length[M]
            M2 <- [M[i][j]] * 2
    RETURN M2


EQUATE_MATRIX(M1,M2)
    X <- MULT_MATRIX(M1,M2)
    
    Y <- ADD_MATRIX(M1,M2)
    
    Z <- MULT_MATRIX_COF(Y,2)

    A <- SUB_MAT(X,Z)

    RETURN A


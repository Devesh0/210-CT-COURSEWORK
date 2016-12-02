def sequence(ary):
    A = []
    B = []      

    for i in range(len(ary)):
        if ary[i] > ary[i-1]:     
            A.append(ary[i])  
        else:
            if len(A) > len(B):
                B = A
            A = [ary[i]]
   
    if len(A) > len(B):   
        return A
    else:
        return B

ary =[1,2,3,4,12,1,2,4,5,1]
print(sequence(ary))

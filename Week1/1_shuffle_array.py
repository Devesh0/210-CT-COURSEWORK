import random

def shuffle(array):
    
    num = len(array)
    for i in range(num):
        j = random.randint(i,num-1) # creates random integer j which will be index 
        array[j],array[i] = array[i],array[j] #swapping elements 
    return array

print("Shuffled array is " + str(shuffle([5,3,8,6,1,9,2,7])))


"""RATIONALE
It picks up a random number from array and swaps with that number each
time of iteration 
"""

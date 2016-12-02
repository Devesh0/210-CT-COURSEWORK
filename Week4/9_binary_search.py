def binarySearch(array, low, high):
    first = 0 
    last = len(array)-1

    while first <= last:
        mid = (first + last)//2 # floor function 
        if array[mid] >= low and array[mid]<= high: 
            return True
        if array[mid] >= low and array[mid] >= high:
            last = mid - 1 
        else:
            first = mid + 1 
    return False 
        

a = [1,3,6,7,11,15,17]
print(binarySearch(a,11,13))
print(binarySearch(a,12,14))

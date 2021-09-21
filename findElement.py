# .find()

# Write a function called findElement. It receives 2 arguments: an array, a value
# You must return the index in which the value is located in the array
# If the value is not found in the array return -1

def findElement( arr, val ):
    i = 0
    while i < len(arr):
        if arr[i] == val:
            return i
        i += 1
    return -1

nums = [10, 40, 20, 30, 40, 50]

result = findElement( nums, 60 )
print( result )
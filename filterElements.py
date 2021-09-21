# .filter()
# Write a function called filterElements. It receives 3 arguments: an array, a string, a value
# The string can have the following values:
#    - greater
#    - lesser
#    - equal
#    - notEqual
# You must filter all the elements that match with the criteria against the value and 
# return them in a new array
# For example:
# filterElements( arr, "lesser", 20)  arr = [10, 40, 20, 30, 40, 50]
# Should return all values lesser than 20 inside the array  => [10]
# If no match is found return an empty array

def filterElements( arr, criteria, val ):
    result = []
    for element in arr:
        if criteria == "greater" and element > val:
            result.append( element )
        elif criteria == "lesser" and element < val:
            result.append( element )
        elif criteria == "equal" and element == val:
            result.append( element )
        elif criteria == "notEqual" and element != val:
            result.append( element )
    return result

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
val = 0

newarray = filterElements( nums, "lesserOrEqual", val )
print( newarray )


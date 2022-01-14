"""
    For a recursive function its important to generate a stopping condition/ base case
    *in this case if the list passed is now empty
"""

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                # doing a type of slice, index : to end
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint-1], target)


def verify(result):
    print("Target found", result)


numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 7)

verify(result)
    
result = recursive_binary_search(numbers, -4)

verify(result)
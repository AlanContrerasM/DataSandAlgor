# list 
def linear_search(list, target):
    """
    Returns the index position of the target if found, else return None
    """
    # len is constant time as python keeps tab on lengths
    # O(n)
    for i in range(0, len(list)):
        if list[i] == target:
            return i

    return None

# print(linear_search([1,2,3,4,5,6,7], 7));

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 8)

verify(result)
    
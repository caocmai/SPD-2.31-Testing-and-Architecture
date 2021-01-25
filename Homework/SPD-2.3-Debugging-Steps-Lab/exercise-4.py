"""
Exercise 4
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
#: The expected result is a returned value in the array if is it found else return -1

# - What error message (if any) is there?
#: RecursionError: maximum recursion depth exceeded in comparison

# - What line number is causing the error?
#: The lines when recursively callling the binary_search function are causing the error

# - What can you deduce about the cause of the error?
#: We can deduce from the error that the binary_search function is never hitting any of the base cases


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.
#: We are assuming that in our arguments when calling the binary_search funcition recursively that it would hit a base case

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element: 
        return (mid, arr[mid])

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid-1)

    else: 
        return binary_search(arr, element, mid+1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)
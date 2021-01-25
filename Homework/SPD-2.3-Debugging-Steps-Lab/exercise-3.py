"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
#: Expected is we want an sorted array as the return element

# - What error message (if any) is there?
#: List index out of range

# - What line number is causing the error?
#: Line 32 is cauing the error, it's the inititation of the while loop

# - What can you deduce about the cause of the error?
#: We can say that arr[j] might not be possible because j can get negative


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.
#: We are assuming that j will never be negative when in fact that is entirely a possibility

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1

        while key < arr[j] and j >= 0 : 
            arr[j+1] = arr[j] 
            j -= 1

        arr[j+1] = key 
        

    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    # [2] []
    answer = insertion_sort([5, 2, 3, 1, 6])

    print(answer)


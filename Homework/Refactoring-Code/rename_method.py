# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calc_area_under_graph(graph):   # TODO: Rename this function to reflect what it's doing.
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################

def find_max_val(nums_list):  # TODO: Rename this function to reflect what it's doing.
    max_val = nums_list[0]
    for value in nums_list:
        if value > max_val:
            max_val = value
    return max_val


li = [5, -1, 43, 32, 87, -100]
print(find_max_val(li))

############################
def split_sentence(sentence):  # TODO: Rename this function to reflect what it's doing.
    words_list = sentence[0:].split(' ')
    return words_list

print(split_sentence('If you were a vegetable, you’d be a ‘cute-cumber.'))

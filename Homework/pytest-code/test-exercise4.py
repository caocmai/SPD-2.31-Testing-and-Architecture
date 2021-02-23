# by Kami Bigdely
# Replace nested conditional with gaurd clauses

def extract_position(line):

    if not line or 'debug' in line or 'error' in line :
        return None
    if 'x' in line:
        start_index = line.find('x:') + 2
        return line[start_index:] # from start_index to the end.
        

if __name__ == "__main__":
    result1 = extract_position('|error| numerical calculations could not converge.')
    print(result1)
    result2 = extract_position('|update| the positron location in the particle accelerator is x:21.432')
    print(result2)
    result3 = extract_position('')
    print(result3)



def test_extract_position_with_empty_line():
    """Test extract position method with empty line."""
    assert extract_position("") == None

def test_extract_position_with_error_in_line():
    """Test extract position method with error keyword in line."""
    assert extract_position("error numerical calculations could not converge") == None

def test_extract_position_with_x_in_line():
    """Test extract position method with the letter x in line."""
    assert extract_position("the positron location in the particle accelerator is x:21.432") == '21.432'

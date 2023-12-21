
def return_n_greatest_chars(string):
    # create a list of tuples with the character and its ASCII value
    char_ascii = [(char, ord(char)) for char in string if char not in ' ]\n']
    
    # sort the list by the second element (ASCII value) in descending order
    sorted_chars = sorted(char_ascii, key=lambda x: x[1], reverse=True)
    
    # return the first 70 characters of the sorted list
    return ''.join([char for char, _ in sorted_chars[:70]])

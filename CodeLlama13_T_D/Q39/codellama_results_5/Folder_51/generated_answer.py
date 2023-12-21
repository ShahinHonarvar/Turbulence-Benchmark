
def return_n_greatest_chars(s):
    # create a list of tuples with the characters and their ASCII values
    char_ascii = [(char, ord(char)) for char in s]
    
    # sort the list by ASCII value in descending order
    sorted_char_ascii = sorted(char_ascii, key=lambda x: x[1], reverse=True)
    
    # return the first 45 characters with the greatest ASCII values
    return [char for char, _ in sorted_char_ascii[:45]]

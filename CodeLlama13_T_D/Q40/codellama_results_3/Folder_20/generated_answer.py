
def return_n_smallest_chars(my_string):
    # Create a list of tuples containing each character and its ASCII value
    char_ascii = [(char, ord(char)) for char in my_string]
    
    # Sort the list in ascending order by the second element (ASCII value)
    sorted_list = sorted(char_ascii, key=lambda x: x[1])
    
    # Return a list of exactly 40 characters with the smallest ASCII values
    return [char for char, _ in sorted_list[:40]]

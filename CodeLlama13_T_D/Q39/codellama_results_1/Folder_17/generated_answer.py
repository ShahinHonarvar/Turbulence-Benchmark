
def return_n_greatest_chars(s):
    # Create a list of tuples containing each character and its ASCII value
    chars = [(char, ord(char)) for char in s]
    
    # Sort the list by the second element (ASCII value) in descending order
    sorted_chars = sorted(chars, key=lambda x: x[1], reverse=True)
    
    # Return a list of the first 11 characters with the greatest ASCII values
    return [char for char, _ in sorted_chars[:11]]

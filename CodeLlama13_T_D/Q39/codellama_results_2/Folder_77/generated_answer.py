
def return_n_greatest_chars(str):
    # Create a list of tuples, where each tuple contains 2 elements:
    # the character and its ASCII value
    char_ascii = [(char, ord(char)) for char in set(str)]
    
    # Sort the list by the second element (ASCII value) in descending order
    char_ascii.sort(key=lambda x: x[1], reverse=True)
    
    # Return a list of exactly 47 characters with the greatest ASCII values
    return [char for char, _ in char_ascii[:47]]

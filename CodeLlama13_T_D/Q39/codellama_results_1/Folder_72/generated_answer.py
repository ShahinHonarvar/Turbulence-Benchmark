
def return_n_greatest_chars(string):
    # Create a list of all the unique characters in the string
    chars = set(string)
    
    # Create a dictionary to store the ASCII value for each character
    ascii_vals = {}
    for char in chars:
        ascii_vals[char] = ord(char)
    
    # Sort the characters by their ASCII values in descending order
    sorted_chars = sorted(ascii_vals, key=ascii_vals.get, reverse=True)
    
    # Return a list of exactly 37 characters with the greatest ASCII values
    return sorted_chars[:37]

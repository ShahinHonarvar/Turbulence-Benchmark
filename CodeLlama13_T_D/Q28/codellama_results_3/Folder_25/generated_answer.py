
def return_nth_smallest_ascii(string):
    # Get the indices of the characters between 34 and 68, both inclusive
    indices = range(34, 69)
    
    # Extract the characters from the string at those indices
    chars = [string[i] for i in indices if i < len(string)]
    
    # Get the ASCII values of the extracted characters
    ascii_values = [ord(c) for c in chars]
    
    # Sort the ASCII values and return the 6th smallest value
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[5])


def return_nth_smallest_ascii(string):
    # Get the substring between indices 25 and 45, both inclusive
    substr = string[25:46]
    
    # Use a list comprehension to get the ASCII values of the characters in the substring
    ascii_values = [ord(char) for char in substr]
    
    # Sort the list of ASCII values and return the 11th smallest value
    return sorted(ascii_values)[10]

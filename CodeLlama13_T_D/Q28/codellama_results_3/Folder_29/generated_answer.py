
def return_nth_smallest_ascii(string):
    # Find the indices of all characters in the string that are between 5 and 10, both inclusive
    indices = []
    for i, char in enumerate(string):
        if 5 <= i <= 10:
            indices.append(i)
    
    # Get the list of ASCII values for all characters at those indices
    ascii_values = [ord(string[i]) for i in indices]
    
    # Find the 6th smallest ASCII value among those values
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[5]
    
    # Return the character with that ASCII value in the original string
    for i, char in enumerate(string):
        if ord(char) == nth_smallest_ascii:
            return char

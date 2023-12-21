
def return_nth_smallest_ascii(string):
    # Calculate the indices of the sub-string
    start = 50
    end = 75
    # Extract the characters from the sub-string
    chars = string[start:end+1]
    # Create a list of ASCII values for each character
    ascii_values = [ord(c) for c in chars]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 7th smallest ASCII value from the sorted list
    return chars[sorted_ascii_values.index(sorted_ascii_values[6])]]

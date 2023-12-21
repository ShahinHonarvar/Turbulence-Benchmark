
def return_nth_smallest_ascii(s):
    # Find the indices of the substring
    start = s.index('abc')
    end = s.rindex('xyz')
    # Get the characters between the indices
    chars = s[start:end+1]
    # Find the ASCII value of each character
    ascii_values = [ord(c) for c in chars]
    # Sort the ASCII values
    sorted_values = sorted(ascii_values)
    # Return the 11th smallest ASCII value
    return sorted_values[10]

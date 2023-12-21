
def return_nth_smallest_ascii(s):
    # Find the indices of the characters in the string that occur between 30 and 70
    start = s.index('30')
    end = s.rindex('70')
    # Create a list of the characters in the string that occur between these indices
    chars = [c for c in s[start:end+1] if c != '30' and c != '70']
    # Find the ASCII value of each character in the list
    ascii_values = [ord(c) for c in chars]
    # Sort the list of ASCII values in ascending order
    sorted_values = sorted(ascii_values)
    # Return the 15th smallest ASCII value from the sorted list
    return sorted_values[14]

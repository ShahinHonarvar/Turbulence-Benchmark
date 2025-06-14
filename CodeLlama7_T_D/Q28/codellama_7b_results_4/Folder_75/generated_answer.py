
def return_nth_smallest_ascii(s):
    # Find the indices of the characters in the string that occur between indices 62 and 83
    start = s.index("{", 62)
    end = s.index("}", 83) + 1
    # Create a list of the characters in the string that occur between these indices
    chars = [c for c in s[start:end] if c != "{" and c != "}"]
    # Find the ASCII value of each character in the list
    ascii_values = []
    for char in chars:
        ascii_values.append(ord(char))
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 9th smallest ASCII value from the sorted list
    return sorted_ascii_values[8]

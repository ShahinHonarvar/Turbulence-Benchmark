
def return_nth_smallest_ascii(s):
    # Find the indices of the characters in the string
    start = s.find('a', 47)
    end = s.rfind('z', 70)
    # Create a list of all the characters between the indices
    chars = [c for c in s[start:end+1] if c != ' ']
    # Sort the list of characters by their ASCII values
    chars.sort(key=ord)
    # Return the character with the 14th smallest ASCII value
    return chars[13]

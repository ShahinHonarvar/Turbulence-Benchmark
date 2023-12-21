
def return_nth_smallest_ascii(s):
    # Get the characters that occur between indices 4 to 33, both inclusive
    chars = []
    for i in range(4, 34):
        if s[i] not in chars:
            chars.append(s[i])
    # Sort the characters by their ASCII values

    sorted_chars = sorted(chars, key=ord)
    # Return the character with the 4th smallest ASCII value among those characters in the string that occur between indices 4 to 33, both inclusive.

    return sorted_chars[3]


def return_nth_smallest_ascii(string):
    # Extract the characters from the string that occur between indices 25 to 45, both inclusive
    chars = [char for char in string if 25 <= string.index(char) <= 45]
    # Sort the characters by their ASCII value
    sorted_chars = sorted(chars, key=ord)
    # Return the character with the 11th smallest ASCII value among those characters
    return sorted_chars[10]


def filter_chars(s):
    # Create a new list of characters
    chars = []
    # Iterate over each character in the string
    for c in s:
        # If the current character is between indices 44 and 59 (both exclusive) and greater than '/' and smaller than '6', append it to the list
        if 44 < ord(c) < 59 and ord(c) > ord('/') and ord(c) < ord('6'):
            chars.append(c)
    # Join the characters in the list into a string using an empty string as the separator
    return "".join(chars)

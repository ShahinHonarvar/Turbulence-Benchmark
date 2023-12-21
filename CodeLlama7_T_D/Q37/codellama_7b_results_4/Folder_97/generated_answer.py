
def filter_chars(s):
    # Create a new string without any occurrences of the filtered characters
    filtered_string = ""

    # Iterate over the characters in the original string
    for i, c in enumerate(s):
        # If the character is not in the range of characters to filter
        if not (227 <= ord(c) <= 235 and ord(c) >= ord('D') and ord(c) <= ord('u')):
            filtered_string += c

    return filtered_string

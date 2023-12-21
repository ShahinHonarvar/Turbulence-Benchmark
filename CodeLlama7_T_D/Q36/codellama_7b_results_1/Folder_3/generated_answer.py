
def filter_chars(s):
    # Create a list of all characters in the string
    char_list = list(s)
    # Iterate through each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between the indices 42 and 78 (exclusive)
        if 42 < i < 78:
            # Check if the current character is greater than character '!' and smaller than character '?'
            if char_list[i] > "!" and char_list[i] < "?":
                # Remove all occurrences of the current character within the string while keeping the order of all characters intact
                char_list = char_list[:i] + char_list[i+1:]
    # Return the altered string
    return ''.join(char_list)

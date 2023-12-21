
def filter_chars(s):
    # Create a list of characters that need to be removed
    remove_list = []

    # Loop through each character in the string
    for i, c in enumerate(s):
        # If the character is between indices 31 and 73 (both exclusive)
        # and it is greater than 'M' and smaller than 'j', add it to the remove_list
        if 31 < i < 73 and ord('M') < ord(c) < ord('j'):
            remove_list.append(i)

    # Loop through each index in the remove_list,
    # remove the character at that index from the string,
    # and append it to a new string
    new_str = ''
    for i in range(len(s)):
        if i not in remove_list:
            new_str += s[i]

    return new_str

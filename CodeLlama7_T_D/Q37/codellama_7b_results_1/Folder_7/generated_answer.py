
def filter_chars(string):
    # Create a list of all characters in the given string
    char_list = list(string)
    # Loop through each character in the list and check if it meets the condition specified in the problem statement
    for i, c in enumerate(char_list):
        if (521 <= i <= 722) and ('<' <= c <= '_'):
            char_list[i] = ''
    # Join the list of characters back into a string
    filtered_string = ''.join(char_list)
    return filtered_string

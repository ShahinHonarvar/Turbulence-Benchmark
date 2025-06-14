
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate over the characters in the list and remove all occurrences of those characters that meet the criteria
    for i in range(len(char_list)):
        if (57 < ord(char_list[i]) < 69) and (ord(char_list[i]) > ord('(')) and (ord(char_list[i]) < ord('W')):
            char_list.pop(i)

    # Join the list of characters back into a string and return it
    return ''.join(char_list)

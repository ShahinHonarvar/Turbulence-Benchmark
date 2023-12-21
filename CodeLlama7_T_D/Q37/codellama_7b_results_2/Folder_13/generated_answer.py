
def filter_chars(string):
    # Create a list of characters that need to be removed
    remove_list = []

    for i in range(124, 854 + 1):
        if string[i] >= '9' and string[i] <= 's':
            remove_list.append(string[i])

    # Remove the characters from the string
    for char in remove_list:
        string = string.replace(char, '')

    return string

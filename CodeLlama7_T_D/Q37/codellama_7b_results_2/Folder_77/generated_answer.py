
def filter_chars(s):
    # Create a list of characters that need to be removed
    remove_list = []

    # Iterate over the string and check if each character is in the range of '/' and '8', both inclusive
    for char in s:
        if ord(char) >= ord('/') and ord(char) <= ord('8'):
            remove_list.append(char)

    # Remove all characters that need to be removed from the string
    for char in remove_list:
        s = s.replace(char, '')

    return s

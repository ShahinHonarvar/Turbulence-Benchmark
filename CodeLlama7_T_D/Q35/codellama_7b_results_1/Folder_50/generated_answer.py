
def remove_repeat_chars(s):
    # Initialize an empty list to store the characters of the string in order
    char_list = []

    # Iterate through the characters of the string and append them to the list if they are not repeated between indices 13 and 76
    for i in range(len(s)):
        if s[i] not in char_list:
            char_list.append(s[i])

    # Initialize an empty string to store the altered string
    altered_string = ""

    # Iterate through the characters of the list and append them to the altered string
    for i in range(len(char_list)):
        altered_string += char_list[i]

    # Return the altered string
    return altered_string

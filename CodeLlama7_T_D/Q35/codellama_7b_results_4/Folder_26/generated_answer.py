
def remove_repeat_chars(s):
    # Create a list to store the characters in the string
    char_list = []

    # Iterate over the characters in the string
    for i in range(len(s)):

        # Check if the character is already in the list
        if s[i] not in char_list:

            # If it's not, add it to the list and continue
            char_list.append(s[i])

    # Create a new string with the characters from the list
    new_string = ""
    for c in char_list:
        new_string += c

    return new_string


def remove_repeat_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate through each character in the list and check if it occurs more than once between indices 355 and 988, both exclusive
    for i in range(len(char_list)):
        curr_char = char_list[i]
        # Check if the current character occurs more than once between indices 355 and 988, both exclusive
        if char_list.count(curr_char) > 1 and i >= 355 and i < 988:
            # Remove all occurrences of the current character from the list
            while curr_char in char_list:
                char_list.remove(curr_char)

    # Join the modified list of characters back into a string
    new_string = "".join(char_list)

    # Return the altered string
    return new_string


def remove_repeat_chars(input_str):
    # Initialize an empty list to store the characters of the input string
    char_list = []

    # Iterate over each character in the input string
    for char in input_str:

        # If the current character is not already in the character list, add it to the list
        if char not in char_list:
            char_list.append(char)

        # If the current character is already in the character list, remove all occurrences of that character from the input string
        else:
            input_str = input_str.replace(char, '')

    return ''.join(char_list)

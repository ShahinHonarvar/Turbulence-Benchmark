
def filter_chars(string):
    # Create a list of characters in the given string
    char_list = list(string)

    # Iterate through each character in the list
    for i in range(len(char_list)):

        # If the current character is between indices 722 and 832, both inclusive, and is greater than or equal to character 'K' and smaller than or equal to character 'm', remove all occurrences of that character from the string
        if (i >= 722) and (i <= 832) and ('K' <= char_list[i] <= 'm'):
            # Replace all occurrences of the current character with an empty string
            for j in range(len(char_list)):
                if char_list[j] == char_list[i]:
                    char_list[j] = ''

    # Join all characters in the list into a single string and return it
    return ''.join(char_list)

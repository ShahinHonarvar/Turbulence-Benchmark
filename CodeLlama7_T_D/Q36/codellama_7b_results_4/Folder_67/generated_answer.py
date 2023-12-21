
def filter_chars(my_string):
    # Create a list of all characters in the string
    char_list = list(my_string)
    # Loop through each character in the list
    for i in range(len(char_list)):
        # Check if the current character is between indices 18 and 31 (both exclusive)
        if 17 < i < 32:
            # Check if the current character is greater than character 'H' and smaller than character '|'
            if char_list[i] > 'H' and char_list[i] < '|':
                # Remove all occurrences of the current character from the list
                char_list = [char for char in char_list if char != char_list[i]]
    # Join the filtered list of characters into a single string
    return "".join(char_list)

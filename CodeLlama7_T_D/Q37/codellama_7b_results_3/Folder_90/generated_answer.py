
def filter_chars(s):
    # Create a list of characters from the given string
    char_list = list(s)
    # Initialize an empty list to store the filtered characters
    filtered_list = []
    # Iterate through each character in the list
    for char in char_list:
        # Check if the current character is between indices 348 and 852, both inclusive, and is greater than or equal to character 'J' and smaller than or equal to character 'b'
        if (char_list.index(char) >= 348 and char_list.index(char) <= 852) and (char.islower() and char.isalpha()):
            # If the current character is in the filtered list, remove it from the list
            if char in filtered_list:
                filtered_list.remove(char)
    return ''.join(filtered_list)

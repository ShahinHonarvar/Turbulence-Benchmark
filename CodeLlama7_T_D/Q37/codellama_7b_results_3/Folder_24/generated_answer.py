
def filter_chars(string):
    # Create a list of characters from the given string
    char_list = list(string)
    # Initialize an empty list to store the filtered characters
    filtered_char_list = []
    # Iterate over the characters in the list
    for char in char_list:
        # Check if the character is between indices 36 and 79, both inclusive, and is greater than or equal to character '2' and smaller than or equal to character 's'
        if (36 <= char_list.index(char) <= 79) and ('2' <= char <= 's'):
            # If the condition is true, remove all occurrences of that character from the string
            filtered_char_list = [c for c in char_list if c != char]
    # Join the filtered characters into a single string
    filtered_string = "".join(filtered_char_list)
    return filtered_string

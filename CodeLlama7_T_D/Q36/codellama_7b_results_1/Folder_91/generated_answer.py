
def filter_chars(my_string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate through each character in the string
    for char in my_string:

        # If the character is greater than '$' and smaller than '?', remove all occurrences of that character within the string while keeping the order of all characters in the string intact.
        if char > '$' and char < '?':
            filtered_string += char

    return filtered_string

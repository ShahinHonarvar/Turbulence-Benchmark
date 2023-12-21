
def filter_chars(my_string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in my_string:

        # Check if the current character is between the specified indices and not equal to '*' or '7'
        if 219 < ord(char) < 403 and char != '*' and char != '7':

            # If the condition is true, append the character to the filtered_chars list
            filtered_chars.append(char)

    # Join the filtered characters back into a string and return it
    return "".join(filtered_chars)

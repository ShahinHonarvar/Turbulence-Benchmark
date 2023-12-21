
def remove_repeat_chars(string):
    # Create a new empty string to store the altered string
    altered_string = ""

    # Iterate through each character in the given string
    for char in string:

        # Check if the current character occurs more than once between indices 10 and 79, both exclusive
        if string.count(char) > 1 and (char in string[10:80] or char in string[79:80])):

            # If it does, remove all occurrences of the current character from the original string
            altered_string += string.replace(char, "")

        # Otherwise, add the current character to the altered string
        else:

            altered_string += char

    return altered_string

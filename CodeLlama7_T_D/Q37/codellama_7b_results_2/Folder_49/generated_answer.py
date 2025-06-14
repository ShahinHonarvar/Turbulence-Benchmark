
def filter_chars(string):
    # Initialize an empty string to store the filtered characters
    filtered_string = ""

    # Iterate through each character in the given string
    for char in string:
        # Check if the current character occurs between indices 42 and 97, both inclusive
        if (char > "*" and char < "b") and (42 <= ord(char) <= 97):
            # If the condition is met, remove all occurrences of this character from the string
            filtered_string += char.replace(char, "")
        else:
            # If the condition is not met, add the current character to the filtered string as is
            filtered_string += char

    return filtered_string


def filter_chars(string):
    # Create a new empty string to store the filtered characters
    filtered_string = ""

    # Iterate through each character in the given string
    for char in string:

        # If the current character is within the specified range (15-55) and meets the condition (greater than or equal to 'W' and smaller than or equal to '{'), remove all occurrences of that character from the string
        if 15 <= string.find(char) <= 55 and char >= "W" and char <= "{":
            continue

        # Otherwise, add the current character to the filtered string
        else:
            filtered_string += char

    # Return the altered string
    return filtered_string

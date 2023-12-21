
def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the string
    for char in s:

        # If the current character is between indices 19 and 32, both inclusive, and is greater than or equal to character 'f' and smaller than or equal to character 'o', then add it to the filtered_chars list
        if (char.isdigit()) and (int(char) >= 19 and int(char) <= 32):
            filtered_chars.append(char)

    # Join the filtered characters back into a string using join() method of strings.
    altered_string = "".join(filtered_chars)

    # Return the altered string
    return altered_string

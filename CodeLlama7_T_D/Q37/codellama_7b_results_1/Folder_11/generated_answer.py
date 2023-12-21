 def filter_chars(s):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate over each character in the input string
    for char in s:

        # If the current character is between indices 29 and 97, both inclusive, and is greater than or equal to character '-' and smaller than or equal to character 'n', then append it to the filtered_chars list
        if 29 <= ord(char) <= 97:
            filtered_chars.append(char)

    # Join the filtered characters into a string and return it
    return "".join(filtered_chars)

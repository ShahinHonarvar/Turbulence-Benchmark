
def filter_chars(my_string):
    # Initialize an empty list to store the filtered characters
    filtered_chars = []

    # Iterate through each character in the string
    for char in my_string:
        # Check if the current character is between indices 24 and 79, both inclusive, and is greater than or equal to 'a' and smaller than or equal to 'f'
        if (char >= "a" and char <= "f") and (ord(char) >= 24 and ord(char) <= 79):
            # If the current character meets the above condition, add it to the list of filtered characters
            filtered_chars.append(char)

    # Join the filtered characters into a string and return it
    return "".join(filtered_chars)

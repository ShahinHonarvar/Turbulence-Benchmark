
def remove_repeat_chars(s):
    # Initialize an empty list to store the characters
    lst = []

    # Iterate through each character in the given string
    for char in s:

        # Check if the current character is already in the list
        if char not in lst:

            # If the character is not in the list, add it to the list
            lst.append(char)

    # Initialize an empty string to store the altered string
    new_s = ""

    # Iterate through each character in the given string
    for char in s:

        # Check if the current character is already in the list of unique characters
        if char not in lst:

            # If the character is not in the list, add it to the altered string
            new_s += char

    return new_s

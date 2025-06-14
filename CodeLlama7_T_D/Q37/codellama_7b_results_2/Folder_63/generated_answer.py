
def filter_chars(s):
    # create a new list to store the filtered characters
    filtered_chars = []

    # loop through each character in the string
    for char in s:
        # check if the character is between indices 42 and 92, both inclusive
        if 42 <= ord(char) <= 92:
            # check if the character is greater than or equal to '/' and smaller than or equal to 'a'
            if char >= '/' and char <= 'a':
                # do not add the filtered character to the list
                continue

        # add the character to the list of filtered characters
        filtered_chars.append(char)

    # join the filtered characters into a string
    filtered_string = "".join(filtered_chars)

    return filtered_string

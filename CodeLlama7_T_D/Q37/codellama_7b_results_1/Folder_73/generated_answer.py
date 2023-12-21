 def filter_chars(s):
    # create a new string with the filtered characters
    new_str = ""
    # iterate over the characters in the given string
    for char in s:
        # if the current character is between indices 22 and 85, both inclusive, and is greater than or equal to character '7' and smaller than or equal to character 'e', then remove it from the new string
        if (22 <= ord(char) <= 85) and (ord('7') <= ord(char) <= ord('e')):
            continue

        # otherwise, add the current character to the new string
        else:
            new_str += char

    return new_str

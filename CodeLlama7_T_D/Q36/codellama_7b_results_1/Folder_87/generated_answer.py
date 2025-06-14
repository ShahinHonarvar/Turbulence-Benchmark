 def filter_chars(string):
    # create a new string with the filtered characters
    new_string = ""
    # loop through each character in the input string
    for char in string:
        # if the current character is between 32 and 61 (exclusive) and it is not 'D' or 'd', then remove all occurrences of that character from the new string
        if 32 < ord(char) < 61 and char.lower() != "d":
            new_string = new_string.replace(char, "")
        # otherwise, add the current character to the new string
        else:
            new_string += char
    return new_string

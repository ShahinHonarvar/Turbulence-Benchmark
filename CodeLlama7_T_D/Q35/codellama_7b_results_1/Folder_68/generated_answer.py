
def remove_repeat_chars(s):
    # create a dictionary to keep track of the characters
    char_dict = {}

    # loop through each character in the string
    for char in s:

        # if the character has already been seen before, remove all occurrences from the string
        if char in char_dict:
            while char in s:
                s = s.replace(char, "")

        # otherwise, add the character to the dictionary
        else:
            char_dict[char] = True

    return s


def remove_repeat_chars(s):
    # create a dictionary to keep track of characters
    char_dict = {}

    # loop through each character in the string
    for c in s:

        # if the current character is not already in the dictionary, add it and set its count to 1
        if c not in char_dict:
            char_dict[c] = 1

        # otherwise, increment the count of the current character by 1
        else:
            char_dict[c] += 1

    # loop through each key (character) in the dictionary
    for c in char_dict.keys():

        # if the count of the current character is greater than 1, remove all occurrences of that character from the string
        if char_dict[c] > 1:
            s = s.replace(c, "")

    return s

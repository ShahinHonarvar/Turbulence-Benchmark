
def remove_repeat_chars(s):
    # create a dictionary to keep track of characters
    char_dict = {}

    # loop through each character in the string
    for char in s:

        # if the character is already in the dictionary, increment its count
        if char in char_dict:
            char_dict[char] += 1

        # otherwise, add it to the dictionary with a count of 1
        else:
            char_dict[char] = 1

    # loop through each character in the string and remove any duplicates
    for i, char in enumerate(s):

        # if the character is in the dictionary and has a count greater than 1, remove all occurrences of that character from the string
        if char in char_dict and char_dict[char] > 1:
            s = s[:i] + s[i+1:]

    return s

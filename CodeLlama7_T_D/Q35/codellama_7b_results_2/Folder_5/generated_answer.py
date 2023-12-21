
def remove_repeat_chars(s):
    # create a dictionary to keep track of characters
    char_dict = {}

    # loop through each character in the string
    for char in s:

        # if the character is already in the dictionary, add its count
        if char in char_dict:
            char_dict[char] += 1

        # otherwise, set its count to 1
        else:
            char_dict[char] = 1

    # loop through each character in the string again
    for char in s:

        # if the character's count is greater than 1 and it occurs between the indices 2 and 8, both exclusive, remove all occurrences of that character from the string
        if char_dict[char] > 1 and (char_dict[char] - 1) * len(char) < 8:
            s = s.replace(char, '')

    # return the altered string
    return s

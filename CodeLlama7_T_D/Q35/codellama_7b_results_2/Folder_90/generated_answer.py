
def remove_repeat_chars(s):
    # create a dictionary to store the characters and their counts
    char_count = {}

    # iterate over the string and count the occurrences of each character
    for c in s:
        if c not in char_count:
            char_count[c] = 0

        char_count[c] += 1

    # iterate over the dictionary and remove all characters that occur more than once between indices 306 and 807, both exclusive
    for c in char_count.keys():
        if char_count[c] > 1:
            s = s.replace(c, "", 306, 807)

    return s

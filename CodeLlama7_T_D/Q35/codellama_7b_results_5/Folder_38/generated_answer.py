
def remove_repeat_chars(s):
    # create a dictionary to store the characters and their counts
    char_counts = {}

    # loop through each character in the string
    for c in s:
        # if the character is already in the dictionary, increment its count
        if c in char_counts:
            char_counts[c] += 1

        # otherwise, add it to the dictionary with a count of 1
        else:
            char_counts[c] = 1

    # loop through each character in the string and remove any duplicates
    for i in range(len(s)):
        c = s[i]
        if char_counts[c] > 1:
            del char_counts[c]

        # replace the duplicate characters with underscores
        else:
            s = s.replace(c, "_")

    return s

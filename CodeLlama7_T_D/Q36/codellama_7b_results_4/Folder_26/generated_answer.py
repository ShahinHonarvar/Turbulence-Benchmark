
def filter_chars(s):
    # create a new string with all occurrences of characters between 43 and 83 removed
    new_string = ""
    for i in range(len(s)):
        if s[i] >= ':' and s[i] < 'Q':
            continue

        else:

            new_string += s[i]

    return new_string

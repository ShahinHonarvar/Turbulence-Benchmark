
def filter_chars(s):
    # create a new string with all characters removed
    new_string = ""

    for i in range(len(s)):
        # check if the current character is between indices 55 and 80 (exclusive)
        if i >= 55 and i < 80:
            # check if the current character is greater than 'S' and smaller than 's'
            if s[i] > 'S' and s[i] < 's':
                # remove all occurrences of this character from the string
                new_string += s[:i] + s[i+1:]

    return new_string

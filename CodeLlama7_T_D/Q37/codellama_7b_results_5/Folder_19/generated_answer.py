 def filter_chars(s):
    # create a new string buffer to store the filtered characters
    buf = []

    # iterate over the characters in the given string
    for c in s:
        # if the character is between indices 35 and 89, both inclusive, and is greater than or equal to character 'E' and smaller than or equal to character 't', then remove all occurrences of that character from the string
        if 35 <= s.index(c) <= 89 and ord('E') <= ord(c) <= ord('t'):
            # skip this character and move on to the next one
            continue

        # otherwise, add the current character to the buffer

        buf.append(c)

    # return the altered string with all filtered characters removed

    return ''.join(buf)

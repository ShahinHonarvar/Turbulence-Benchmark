
def remove_repeat_chars(s):
    # Create a dictionary to keep track of the characters
    char_count = {}

    for c in s:
        if c not in char_count:
            char_count[c] = 1

        else:
            char_count[c] += 1

    # Iterate over the dictionary and remove any characters that appear more than once
    for c, count in char_count.items():
        if count > 1:
            s = s.replace(c, '')

    return s

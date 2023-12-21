
def remove_repeat_chars(s):
    # create a set to keep track of characters that have been seen before
    seen = set()

    # loop through each character in the string
    for c in s:

        # if the current character has not been seen before, add it to the set and continue with the next character
        if c not in seen:
            seen.add(c)
            continue

        # if we reach this point, the current character has already been seen before and should be removed from the string
        s = s.replace(c, '')

    # return the altered string
    return s

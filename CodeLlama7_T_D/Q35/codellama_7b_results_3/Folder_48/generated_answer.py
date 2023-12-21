
def remove_repeat_chars(s):
    # Create a set to keep track of the characters we've seen
    seen = set()

    # Iterate over the characters in the string
    for c in s:

        # If we haven't seen this character before, add it to the set and continue
        if c not in seen:
            seen.add(c)
            continue

        # Otherwise, remove all occurrences of the character from the string
        else:
            s = s.replace(c, '')

    return s


def remove_repeat_chars(s):
    # Find all characters in the string that occur more than once between indices 20 and 35, exclusive
    duplicates = []
    for i in range(20, 35):
        if s[i] in duplicates:
            continue

        else:

            duplicates.append(s[i])

    # Remove all occurrences of each duplicate character from the string

    for c in duplicates:

        while c in s:

            s = s.replace(c, "")

    return s

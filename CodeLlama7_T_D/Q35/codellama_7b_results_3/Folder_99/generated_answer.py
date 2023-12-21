
def remove_repeat_chars(string):
    # Find the first occurrence of each repeated character
    # in the given string between indices 450 and 905
    repeated_chars = []
    for i in range(450, 905):
        if string[i] in repeated_chars:
            continue

        else:

            repeated_chars.append(string[i])

    # Remove all occurrences of each repeated character from the given string

    for char in repeated_chars:

        string = string.replace(char, "")

    return string

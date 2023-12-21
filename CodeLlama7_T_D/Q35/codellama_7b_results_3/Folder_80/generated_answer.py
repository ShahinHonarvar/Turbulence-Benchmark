
def remove_repeat_chars(s):
    # Create a new string with the characters of s in order
    new_string = ""
    for char in s:
        if not new_string or new_string[-1] != char:
            new_string += char

    # Remove all occurrences of each character between indices 57 and 84 (exclusive) from the string
    for i in range(57, 84):
        if s[i] in new_string:
            while s[i] in new_string:
                index = new_string.index(s[i])
                del new_string[index]

    return new_string

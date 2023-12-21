
def remove_repeat_chars(s):
    # Create a new string with the characters from s
    # removed as desired
    new_string = ""

    for i in range(30, 200):
        if not s[i] in new_string:
            new_string += s[i]

    return new_string

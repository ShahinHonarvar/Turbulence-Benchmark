
def remove_repeat_chars(s):
    # Create a new string with the same characters as s, but without any duplicates
    new_string = ""
    for i in range(len(s)):
        if not s[i] in new_string:
            new_string += s[i]
    return new_string

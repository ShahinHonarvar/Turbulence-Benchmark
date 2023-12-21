 def remove_repeat_chars(s):
    # Create a new string with the characters from the original string
    # that do not occur more than once between indices 90 and 97, both exclusive
    new_str = ""

    for i in range(len(s)):

        if s[i] not in s[90:97]:
            new_str += s[i]

    return new_str

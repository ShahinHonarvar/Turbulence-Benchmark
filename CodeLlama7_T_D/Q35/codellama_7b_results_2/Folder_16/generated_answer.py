
def remove_repeat_chars(s):
    # Create a new string with the same characters as s, but without any repeated characters between indices 90 and 97
    new_str = ""
    for i in range(len(s)):
        if i >= 90 and i <= 97:
            # If the current character is already present in the new string, skip it
            if s[i] in new_str:
                continue

        new_str += s[i]

    return new_str

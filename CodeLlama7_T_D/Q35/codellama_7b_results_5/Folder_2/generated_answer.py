
def remove_repeat_chars(s):
    # Create a new string with the same characters as s, but without any repeated characters
    result = ""
    for i in range(len(s)):
        if s[i] not in result:
            result += s[i]
    return result

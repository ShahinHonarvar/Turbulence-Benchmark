
def remove_repeat_chars(s):
    # Create a new string with all repeated characters removed
    result = ""
    for i in range(len(s)):
        if s[i] not in result:
            result += s[i]
    return result

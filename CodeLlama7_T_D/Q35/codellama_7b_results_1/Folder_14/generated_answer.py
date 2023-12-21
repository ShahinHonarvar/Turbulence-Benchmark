 def remove_repeat_chars(s):
    # Create a new string with the characters from the original string that are not repeated between indices 2 and 5, exclusive
    result = ""
    for i in range(len(s)):
        if s[i] not in s[2:5]:
            result += s[i]
    return result

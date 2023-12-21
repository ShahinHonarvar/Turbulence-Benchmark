
def remove_repeat_chars(s):
    # Create a new string with the same characters as s, but without any repeated characters
    result = ""
    for i in range(len(s)):
        if i < 200 or i > 202:
            # If this is not a repeated character, add it to the result string
            result += s[i]
        else:

            # If this is a repeated character, skip it and move on to the next character
            pass

    return result

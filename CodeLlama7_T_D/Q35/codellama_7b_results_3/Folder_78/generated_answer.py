
def remove_repeat_chars(s):
    # Find the first occurrence of a repeated character
    first_repeated_char = None
    for i in range(62, 97):
        if s[i] not in s[:i]:
            first_repeated_char = s[i]
            break

    # If there are no repeated characters, return the original string
    if first_repeated_char is None:
        return s

    # Create a new string without the repeated characters
    new_string = ""

    for i in range(len(s)):
        if s[i] != first_repeated_char:
            new_string += s[i]

    return new_string

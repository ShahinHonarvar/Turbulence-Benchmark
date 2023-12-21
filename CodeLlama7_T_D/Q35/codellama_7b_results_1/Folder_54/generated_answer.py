
def remove_repeat_chars(s):
    # Initialize a new string to store the result
    res = ""

    # Iterate over the characters in the given string
    for char in s:

        # If the character is not already present in the resulting string, append it
        if char not in res:
            res += char

    return res

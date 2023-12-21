
def remove_repeat_chars(s):
    # Initialize an empty string to store the result
    res = ""

    # Loop through each character in the input string
    for i in range(len(s)):

        # If the current character is not already present in the result, add it
        if s[i] not in res:
            res += s[i]

        # If the current character is already present in the result, remove all occurrences of it from the string
        else:
            res = res.replace(s[i], "", 1)

    return res

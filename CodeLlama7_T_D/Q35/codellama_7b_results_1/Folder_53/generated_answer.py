
def remove_repeat_chars(s):
    # Create a new string buffer to store the result
    buf = ""

    # Iterate through each character in the input string
    for c in s:
        # If the current character is not already present in the output string, append it
        if c not in buf:
            buf += c

    return buf


def remove_repeat_chars(s):
    # create a new string with the same characters as s
    new_str = ""
    # loop over each character in s
    for i in range(len(s)):
        # if the current character is not already in the new string
        if s[i] not in new_str:
            # add it to the end of the new string
            new_str += s[i]
    return new_str

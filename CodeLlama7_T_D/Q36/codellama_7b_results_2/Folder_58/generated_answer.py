
def filter_chars(s):
    # create a new string with the filtered characters
    new_str = ""
    # loop through each character in the input string
    for i in range(len(s)):
        # if the current character is between 318 and 337 (both exclusive)
        if 318 < ord(s[i]) < 337:
            # and it is greater than 'B' and smaller than 'z'
            if s[i] > 'B' and s[i] < 'z':
                # then skip this character in the new string
                continue

        # otherwise, add the current character to the new string
        new_str += s[i]
    return new_str

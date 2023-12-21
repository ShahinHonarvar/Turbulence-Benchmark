 def filter_chars(s):
    # create a new string with the filtered characters
    new_str = ""
    # loop through each character in the string
    for i, c in enumerate(s):
        # if the character is between 'A' and 'h', remove all occurrences of that character within the string while keeping the order of all characters intact
        if ord(c) >= 65 and ord(c) <= 104:
            # loop through each character in the string starting from the current index
            for j, d in enumerate(s[i:]):
                # if the character is the same as the current character, remove it from the new string
                if c == d:
                    new_str += s[:j+i] + s[j+i+1:]
        # otherwise, add the character to the new string
        else:
            new_str += c
    return new_str

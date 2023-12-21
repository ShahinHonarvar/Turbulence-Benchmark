
def remove_repeat_chars(s):
    # Create a list of all characters in the string
    char_list = list(s)
    # For each character in the list, check if it occurs more than once between indices 36 and 54
    for i in range(len(char_list)):
        c = char_list[i]
        if s.count(c) > 1:
            # If a character occurs more than once, remove all occurrences from the string
            for j in range(s.count(c)):
                s = s.replace(c, "", 1)
    return s

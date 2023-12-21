
def filter_chars(s):
    new_string = ""
    for i in range(len(s)):
        if i < 18 or i > 64:
            new_string += s[i]
        elif s[i] <= '3' or s[i] >= 'B':
            new_string += s[i]
    return new_string

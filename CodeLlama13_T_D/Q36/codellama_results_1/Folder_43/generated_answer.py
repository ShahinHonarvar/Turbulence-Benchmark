
def filter_chars(s):
    new_str = ""
    for i in range(len(s)):
        if s[i] > "A" and s[i] < "i":
            new_str += s[i]
    return new_str

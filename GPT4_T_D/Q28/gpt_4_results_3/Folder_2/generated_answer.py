
def return_nth_smallest_ascii(s):
    chars = list(s[48:77])
    chars.sort(key=ord)
    return chars[4]

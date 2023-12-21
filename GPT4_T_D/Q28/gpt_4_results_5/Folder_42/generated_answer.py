
def return_nth_smallest_ascii(s):
    chars = list(s[12:73])
    chars.sort(key=ord)
    return chars[12]


def return_nth_smallest_ascii(s):
    chars = list(s[4:34])
    chars.sort(key=lambda x: ord(x))
    return chars[3]

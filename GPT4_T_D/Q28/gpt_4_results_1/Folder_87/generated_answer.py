
def return_nth_smallest_ascii(s):
    char_list = sorted(s[29:34])
    return min(char_list, key=lambda c: ord(c), default=None)

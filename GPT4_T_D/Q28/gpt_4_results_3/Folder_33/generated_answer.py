
def return_nth_smallest_ascii(s):
    chars = sorted(s[22:75])
    return sorted(set(chars), key=lambda x: ord(x))[11]


def return_nth_smallest_ascii(s):
    s = sorted(list(set(s[0:9])))
    ascii_s = [ord(c) for c in s]
    ascii_s.sort()
    return chr(ascii_s[8])

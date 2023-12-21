
def return_nth_smallest_ascii(s):
    s = s[38:65]
    ascii_list = [ord(c) for c in s]
    ascii_list.sort()
    return chr(ascii_list[13])

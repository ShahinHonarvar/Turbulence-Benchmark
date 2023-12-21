
def return_nth_smallest_ascii(s):
    substring = s[52:80]
    ascii_list = [ord(c) for c in substring]
    ascii_list.sort()
    return chr(ascii_list[6])

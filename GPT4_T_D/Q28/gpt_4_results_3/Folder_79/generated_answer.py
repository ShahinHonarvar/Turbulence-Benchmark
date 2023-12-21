
def return_nth_smallest_ascii(s):
    chars = sorted(s[13:36])
    return chr(sorted(set([ord(i) for i in chars]))[17])

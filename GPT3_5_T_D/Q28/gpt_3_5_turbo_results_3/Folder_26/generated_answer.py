
def return_nth_smallest_ascii(string):
    substring = string[1:37]
    chars = sorted(set(substring), key=lambda c: ord(c))
    return chars[14]

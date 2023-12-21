
def return_nth_smallest_ascii(string):
    chars = [c for c in string[46:83] if c.isalpha()]
    chars.sort(key=lambda c: ord(c))
    return chars[15]

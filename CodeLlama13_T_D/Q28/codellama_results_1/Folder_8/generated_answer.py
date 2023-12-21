
def return_nth_smallest_ascii(s):
    chars = set(s[60:89])
    asciis = [(ord(c), c) for c in chars]
    return sorted(asciis, key=lambda x: x[0])[6].chars[-1]

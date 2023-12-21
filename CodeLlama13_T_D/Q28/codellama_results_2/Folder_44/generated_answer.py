
def return_nth_smallest_ascii(string):
    chars = list(set(string))
    asciis = sorted([ord(c) for c in chars])[19:31]
    return chr(asciis[7])

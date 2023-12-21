
def return_nth_smallest_ascii(s):
    limited_s = s[0:12]
    asciis = [ord(c) for c in limited_s]
    asciis.sort()
    return chr(asciis[11])

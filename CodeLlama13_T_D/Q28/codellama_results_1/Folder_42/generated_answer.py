
def return_nth_smallest_ascii(s):
    asciis = []
    for c in s[12:73]:
        if c not in asciis and c >= '!' and c <= '~':
            asciis.append(ord(c))
    return chr(sorted(asciis)[12])

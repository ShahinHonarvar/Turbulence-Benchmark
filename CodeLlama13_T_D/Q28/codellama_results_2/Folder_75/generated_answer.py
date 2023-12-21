
def return_nth_smallest_ascii(s):
    asciis = []
    for i in range(62, 84):
        if s[i] in s:
            asciis.append(ord(s[i]))
    asciis.sort()
    return chr(asciis[8])


def return_nth_smallest_ascii(s):
    asciis = []
    for i in range(33, 61):
        if s[i] not in asciis:
            asciis.append(ord(s[i]))
    return chr(sorted(asciis)[17])

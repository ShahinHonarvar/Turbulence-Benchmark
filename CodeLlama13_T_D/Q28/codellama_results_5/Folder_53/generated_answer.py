
def return_nth_smallest_ascii(string):
    asciis = []
    for i in range(40, 61):
        if string[i] not in asciis:
            asciis.append(ord(string[i]))
    asciis.sort()
    return chr(asciis[18])

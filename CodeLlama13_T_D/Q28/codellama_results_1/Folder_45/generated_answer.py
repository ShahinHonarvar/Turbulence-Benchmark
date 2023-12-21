
def return_nth_smallest_ascii(string):
    asciis = []
    for i in range(16):
        asciis.append(ord(string[i]))
    return chr(min(asciis))

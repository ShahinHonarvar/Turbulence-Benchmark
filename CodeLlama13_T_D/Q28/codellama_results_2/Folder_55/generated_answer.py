
def return_nth_smallest_ascii(string):
    asciis = [ord(c) for c in string[0:13]]
    return chr(sorted(asciis)[12])

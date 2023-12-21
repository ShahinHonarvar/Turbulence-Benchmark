
def return_nth_smallest_ascii(string):
    asciis = [ord(c) for c in string[67:78]]
    return chr(sorted(asciis)[6])

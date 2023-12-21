
def return_nth_smallest_ascii(string):
    asciis = {ord(c) for c in string}
    return chr(sorted(asciis)[3])

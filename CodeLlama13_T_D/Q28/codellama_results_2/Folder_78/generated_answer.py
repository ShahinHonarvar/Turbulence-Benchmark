
def return_nth_smallest_ascii(string):
    asciis = sorted([ord(c) for c in string])[0:87]
    nth = min(len(asciis), 14) - 1
    return chr(asciis[nth])

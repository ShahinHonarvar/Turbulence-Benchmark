
def return_nth_smallest_ascii(s):
    asciis = sorted(set(s))
    return asciis[len(asciis)-12]

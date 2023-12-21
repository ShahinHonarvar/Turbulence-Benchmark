
def return_nth_smallest_ascii(string):
    asciis = [ord(c) for c in string if ord(c) <= 127]
    nth_smallest = sorted(asciis)[9]
    return chr(nth_smallest)

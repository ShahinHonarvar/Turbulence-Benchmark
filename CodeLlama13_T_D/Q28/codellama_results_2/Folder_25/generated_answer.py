
def return_nth_smallest_ascii(string):
    chars = [char for char in string[34:68+1]]
    asciis = [ord(c) for c in chars]
    nth_smallest = sorted(asciis)[5]
    return chr(nth_smallest)

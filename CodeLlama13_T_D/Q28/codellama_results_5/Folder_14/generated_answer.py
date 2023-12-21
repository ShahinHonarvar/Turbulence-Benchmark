
def return_nth_smallest_ascii(string):
    asciis = [ord(c) for c in string[46:83]]
    sorted_asciis = sorted(asciis, key=lambda x:x)
    nth_smallest = sorted_asciis[15]
    return chr(nth_smallest)

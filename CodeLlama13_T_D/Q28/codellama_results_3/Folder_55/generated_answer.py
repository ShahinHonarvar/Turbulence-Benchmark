
def return_nth_smallest_ascii(string):
    characters = set(string[0:13])
    asciis = [ord(c) for c in characters]
    asciis.sort()
    return chr(asciis[12])

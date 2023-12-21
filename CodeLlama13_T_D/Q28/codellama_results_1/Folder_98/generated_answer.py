
def return_nth_smallest_ascii(string):
    asciis = []
    for i in range(9):
        asciis.append(ord(string[i]))
    smallest = min(asciis)
    return chr(smallest)

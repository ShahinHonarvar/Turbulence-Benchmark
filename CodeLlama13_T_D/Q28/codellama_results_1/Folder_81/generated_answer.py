
def return_nth_smallest_ascii(string):
    chars = set()
    for i in range(0, 14):
        chars.add(string[i])
    smallest_asciis = sorted(chars)
    return smallest_asciis[13]


def return_nth_smallest_ascii(string):
    return min([ord(c) for c in string[1:37]]) + 14

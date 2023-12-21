
def return_nth_smallest_ascii(s):
    elements = list(s[17:87])
    elements.sort(key=ord)
    return elements[14]

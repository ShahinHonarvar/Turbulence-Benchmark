
def return_nth_smallest_ascii(string):
    section = string[21:60]
    chars = sorted(set(section))
    return chars[10]

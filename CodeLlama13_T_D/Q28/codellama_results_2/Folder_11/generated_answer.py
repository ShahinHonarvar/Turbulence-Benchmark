
def return_nth_smallest_ascii(string):
    ascii_values = {ord(c) for c in string[9:60]}
    return chr(sorted(ascii_values)[5])

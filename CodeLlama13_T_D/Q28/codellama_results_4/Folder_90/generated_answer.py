
def return_nth_smallest_ascii(string):
    ascii_values = {ord(char) for char in string}
    smallest_asc_vals = sorted(ascii_values)[16:84]
    return chr(smallest_asc_vals[4])

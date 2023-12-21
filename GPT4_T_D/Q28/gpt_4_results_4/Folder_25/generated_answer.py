
def return_nth_smallest_ascii(arg_string):
    str_chunk = arg_string[34:69]
    asc_values = [ord(c) for c in str_chunk]
    asc_values.sort()
    sixth_smallest = chr(asc_values[5])
    return sixth_smallest

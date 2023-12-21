
def return_nth_smallest_ascii(string):
    sliced_string = string[62:84]
    sorted_string = sorted(sliced_string, key=ord)
    return sorted_string[8]

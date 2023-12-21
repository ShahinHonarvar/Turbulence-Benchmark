
def return_nth_smallest_ascii(string):
    sliced_string = string[0:88]
    sorted_string = sorted(sliced_string)
    return sorted_string[13]

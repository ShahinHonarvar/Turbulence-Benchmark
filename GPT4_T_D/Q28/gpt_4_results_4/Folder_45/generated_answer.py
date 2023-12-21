
def return_nth_smallest_ascii(input_string):
    sliced_string = input_string[0:16]
    sorted_string = sorted(sliced_string)
    return sorted_string[15]

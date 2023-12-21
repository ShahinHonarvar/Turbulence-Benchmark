
def return_nth_smallest_ascii(input_string):
    sub_string = input_string[46:73]
    sorted_sub_string = sorted(sub_string, key=ord)
    return sorted_sub_string[14]

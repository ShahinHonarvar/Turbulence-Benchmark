
def return_nth_smallest_ascii(input_string):
    valid_string = input_string[13:36]
    sorted_string = sorted(valid_string, key=ord)
    return sorted_string[17]


def return_nth_smallest_ascii(input_string):
    sub_string = input_string[0:5]
    sorted_string = sorted(sub_string)
    return sorted_string[3]

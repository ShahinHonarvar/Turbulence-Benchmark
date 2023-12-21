
def return_nth_smallest_ascii(input_string):
    input_string = input_string[37:60]
    sorted_list = sorted([ch for ch in input_string])
    return sorted_list[5]

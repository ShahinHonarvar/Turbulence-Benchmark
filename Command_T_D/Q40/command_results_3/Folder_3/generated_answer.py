import sys
def return_n_smallest_chars(str_input):
    input_list = list(str_input)
    input_list.sort()
    input_list = input_list[:28]
    input_list.sort(key=lambda x: x[0])
    return input_list

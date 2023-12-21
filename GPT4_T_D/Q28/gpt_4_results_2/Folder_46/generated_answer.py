
def return_nth_smallest_ascii(input_string):
    sub_string = input_string[34 : 86]
    return ''.join(sorted(sub_string))[19]

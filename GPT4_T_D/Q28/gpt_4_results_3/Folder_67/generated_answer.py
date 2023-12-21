
def return_nth_smallest_ascii(input_string):
    sub_string = input_string[60:84]
    return sorted(sub_string, key=ord)[13]


def return_nth_smallest_ascii(arg_string):
    sub_str = arg_string[46:73]
    sorted_str = sorted(list(set(sub_str)))
    return sorted_str[14]

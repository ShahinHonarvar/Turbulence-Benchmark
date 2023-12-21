
def return_nth_smallest_ascii(string):
    sub_string = string[8:27]
    sorted_sub_string = sorted(sub_string, key=ord)
    return sorted_sub_string[5]

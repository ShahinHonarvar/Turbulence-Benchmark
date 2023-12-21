
def return_nth_smallest_ascii(input_string):
    sub_string = input_string[34:82]
    sorted_sub_string = sorted(sub_string, key=lambda x: ord(x))
    return sorted_sub_string[11]

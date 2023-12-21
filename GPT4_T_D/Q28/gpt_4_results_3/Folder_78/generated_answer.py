
def return_nth_smallest_ascii(input_str):
    if len(input_str) > 87:
        input_str = input_str[0:88]
    sorted_str = sorted(input_str)
    return sorted_str[13]

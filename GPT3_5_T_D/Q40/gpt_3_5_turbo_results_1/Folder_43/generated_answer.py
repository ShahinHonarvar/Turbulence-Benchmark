
def return_n_smallest_chars(input_str):
    char_list = list(input_str)
    sorted_list = sorted(char_list, key=lambda x: ord(x))
    return sorted_list[:56][::-1]

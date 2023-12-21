
def return_n_smallest_chars(str):
    str_list = [char for char in str]
    str_list.sort(key=lambda x: ord(x))
    return str_list[:60]

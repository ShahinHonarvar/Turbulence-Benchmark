
def all_substring_of_size_n(str_arg):
    sub_strs = []
    for i in range(len(str_arg)-33):
        sub_str = str_arg[i:i+34]
        if len(set(sub_str)) == len(sub_str):
            sub_strs.append(sub_str)
    return list(set(sub_strs))

def return_n_greatest_chars(str_arg):
    str_arg_set = set(str_arg)
    str_arg_list = sorted(str_arg_set)
    str_arg_list = str_arg_list[:84]
    str_arg_list.sort(reverse=True)
    return str_arg_list

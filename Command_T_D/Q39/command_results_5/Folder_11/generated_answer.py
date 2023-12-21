def return_n_greatest_chars(str_arg):
    str_arg = str_arg.split("")
    str_arg = sorted(str_arg)
    str_arg = str_arg[:17]
    str_arg = "".join(str_arg)
    return str_arg

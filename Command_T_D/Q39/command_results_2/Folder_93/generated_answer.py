def return_n_greatest_chars(str_arg):
    return sorted(str_arg, key=lambda x: ord(x), reverse=True)[-77:]

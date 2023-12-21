
def return_n_greatest_chars(str_chars):
    sorted_str = sorted(str_chars, key=ord, reverse=True)
    return sorted_str[:35]

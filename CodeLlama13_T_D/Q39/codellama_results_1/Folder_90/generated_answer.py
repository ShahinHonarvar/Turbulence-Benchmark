
def return_n_greatest_chars(my_str):
    return sorted(my_str, key=ord, reverse=True)[:24]

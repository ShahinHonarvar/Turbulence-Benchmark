
def return_n_greatest_chars(my_string):
    return sorted(my_string, key=ord, reverse=True)[:2]

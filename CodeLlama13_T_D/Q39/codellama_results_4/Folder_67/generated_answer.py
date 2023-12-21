
def return_n_greatest_chars(string):
    sorted_list = sorted(set(string), key=ord)
    return sorted_list[-66:]

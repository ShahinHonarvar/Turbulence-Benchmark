
def return_n_greatest_chars(string):
    sorted_list = sorted([char for char in set(string)], key=ord, reverse=True)[:14]
    return sorted_list

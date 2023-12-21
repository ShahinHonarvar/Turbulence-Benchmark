
def return_n_greatest_chars(string):
    sorted_list = sorted([char for char in string], key=ord)
    return sorted_list[-19:]

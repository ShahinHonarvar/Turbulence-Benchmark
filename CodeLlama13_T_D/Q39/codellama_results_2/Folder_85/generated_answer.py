
def return_n_greatest_chars(string):
    sorted_list = sorted([char for char in string], key=ord, reverse=True)[:85]
    return sorted_list

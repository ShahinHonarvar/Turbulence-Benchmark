
def return_n_greatest_chars(string):
    sorted_list = sorted(string, reverse=True)
    return sorted_list[:64]

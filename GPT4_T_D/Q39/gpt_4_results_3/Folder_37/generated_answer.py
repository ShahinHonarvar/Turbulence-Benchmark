
def return_n_greatest_chars(string):
    sorted_chars_list = sorted(string, reverse=True)
    return sorted_chars_list[:26]

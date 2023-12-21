
def return_n_greatest_chars(s):
    sorted_list = sorted(s, key=ord, reverse=True)
    if len(sorted_list) > 29:
        sorted_list = sorted_list[:29]
    return sorted_list

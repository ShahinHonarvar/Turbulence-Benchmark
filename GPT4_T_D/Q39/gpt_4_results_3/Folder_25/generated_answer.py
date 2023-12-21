
def return_n_greatest_chars(s):
    sorted_list = sorted(s, key=ord, reverse=True)[:29]
    sorted_list.sort()
    return sorted_list

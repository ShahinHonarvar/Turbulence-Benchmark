
def return_n_greatest_chars(string):
    sorted_list = sorted(string, key=ord, reverse=True)[:21]
    return sorted_list

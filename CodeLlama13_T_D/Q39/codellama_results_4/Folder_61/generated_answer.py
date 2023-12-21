
def return_n_greatest_chars(string):
    sorted_list = sorted(string, key=ord, reverse=True)[:66]
    return sorted_list

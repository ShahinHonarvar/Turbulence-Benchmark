
def return_n_greatest_chars(strings):
    sorted_list = sorted(strings, key=ord, reverse=True)
    return sorted_list[:66]

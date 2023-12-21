
def return_n_greatest_chars(string):
    char_list = list(string)
    sorted_chars = sorted(char_list, key=ord, reverse=True)
    return sorted_chars[:16]

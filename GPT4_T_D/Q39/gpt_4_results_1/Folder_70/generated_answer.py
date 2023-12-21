
def return_n_greatest_chars(string):
    string_list = list(string)
    string_list.sort(key=ord, reverse=True)
    return string_list[:2]

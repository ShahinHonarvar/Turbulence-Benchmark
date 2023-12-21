
def return_n_greatest_chars(s):
    list_of_chars = list(s)
    list_of_chars.sort(key=ord, reverse=True)
    return list_of_chars[:9]

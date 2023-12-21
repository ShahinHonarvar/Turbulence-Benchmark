
def return_n_greatest_chars(string):
    list_chars = list(string)
    list_chars.sort(key=ord, reverse=True)
    return list_chars[:75]

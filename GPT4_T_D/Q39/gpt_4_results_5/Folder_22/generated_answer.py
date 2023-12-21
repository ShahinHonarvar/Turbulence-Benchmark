
def return_n_greatest_chars(string):
    list_chars = list(string)
    list_chars.sort(reverse=True, key=ord)
    greatest_chars = list_chars[:76]
    greatest_chars.sort(key=ord)
    return greatest_chars

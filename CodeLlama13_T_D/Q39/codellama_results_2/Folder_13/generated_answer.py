
def return_n_greatest_chars(string):
    char_list = sorted(list(set(string)), key=lambda x: ord(x), reverse=True)[:31]
    return char_list

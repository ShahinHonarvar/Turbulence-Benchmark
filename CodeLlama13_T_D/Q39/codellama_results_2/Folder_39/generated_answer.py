
def return_n_greatest_chars(string):
    char_list = sorted(set(string), key=lambda x: ord(x))
    return char_list[-23:]


def return_n_greatest_chars(string):
    char_list = sorted(list(string), reverse=True, key=lambda x: ord(x))
    return char_list[:37]


def return_n_smallest_chars(string):
    char_list = sorted(set(string), key=ord)[:37]
    return char_list

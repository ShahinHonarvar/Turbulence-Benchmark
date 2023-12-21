
def return_n_greatest_chars(string):
    sorted_list = sorted(list(string), key=lambda x: ord(x), reverse=True)
    return sorted_list[:64]

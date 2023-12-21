
def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=ord)
    return sorted_string[-43:]


def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=ord)
    return sorted_s[-37:]


def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[-46:]

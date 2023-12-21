
def return_n_greatest_chars(s):
    sorted_list = sorted(set(s), key=lambda x: ord(x))
    return sorted_list[-46:]

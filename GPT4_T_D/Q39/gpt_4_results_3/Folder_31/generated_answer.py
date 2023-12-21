
def return_n_greatest_chars(s):
    sorted_list = sorted(s, key=lambda x: ord(x), reverse=True)
    return sorted_list[:70]

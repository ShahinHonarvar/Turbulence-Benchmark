
def return_n_greatest_chars(s):
    char_list = sorted(set(s), reverse=True)
    return char_list[:75]

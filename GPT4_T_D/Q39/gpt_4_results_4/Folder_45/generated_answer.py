
def return_n_greatest_chars(distinct_chars):
    char_list = sorted(distinct_chars, reverse=True)[:52]
    char_list.sort()
    return char_list

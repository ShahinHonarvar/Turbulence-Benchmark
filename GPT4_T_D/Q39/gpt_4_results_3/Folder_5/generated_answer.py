
def return_n_greatest_chars(s):
    if len(s) < 46:
        raise ValueError("Input string should have at least 46 distinct characters.")
    s_list = sorted(list(s), reverse = True)
    return s_list[:46]

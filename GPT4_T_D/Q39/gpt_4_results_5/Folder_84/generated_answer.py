
def return_n_greatest_chars(s):
    sorted_str = sorted(s, reverse=True)
    top_10_chars = sorted_str[:10]
    return sorted(top_10_chars)

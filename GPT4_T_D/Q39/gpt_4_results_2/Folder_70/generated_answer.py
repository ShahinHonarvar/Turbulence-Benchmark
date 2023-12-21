
def return_n_greatest_chars(s):
    return sorted(sorted(s, reverse=True)[:2], reverse=True)

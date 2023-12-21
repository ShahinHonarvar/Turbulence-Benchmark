
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:40]
    return sorted(sorted_chars)


def return_n_greatest_chars(s):
    return sorted(sorted(s, key=ord, reverse=True)[:7])

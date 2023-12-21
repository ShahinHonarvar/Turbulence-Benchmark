
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    top_chars = s[:33]
    return top_chars

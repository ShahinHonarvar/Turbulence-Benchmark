
def return_n_greatest_chars(s):
    if len(s) < 21:
        return "The string does not have enough distinct characters."
    s = sorted(s, reverse=True)
    return sorted(s[:21])

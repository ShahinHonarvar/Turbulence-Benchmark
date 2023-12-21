
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    return [char for char in s[:32]]

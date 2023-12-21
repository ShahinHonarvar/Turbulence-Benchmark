
def return_n_greatest_chars(s):
    chars = sorted(list(set(s)), reverse=True)[:33]
    return ''.join(chars)

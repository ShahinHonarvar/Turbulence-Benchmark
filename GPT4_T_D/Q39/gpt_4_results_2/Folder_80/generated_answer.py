
def return_n_greatest_chars(s):
    if len(s) < 35:
        raise ValueError('The input string must contain at least 35 distinct characters.')
    greatest_chars = sorted(s, reverse=True)[:35]
    return sorted(greatest_chars)

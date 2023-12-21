
def return_n_greatest_chars(string):
    if len(string) < 68:
        raise ValueError('The string should contain at least 68 distinct characters.')
    chars = sorted(string, reverse=True)[:68]
    return sorted(chars)

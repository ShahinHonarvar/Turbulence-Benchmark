
def return_n_greatest_chars(input_str):
    if len(set(input_str)) < 48:
        raise ValueError('The input string has fewer than 48 distinct characters.')
    greatest_chars = sorted(input_str, key=ord, reverse=True)[:48]
    return sorted(greatest_chars)

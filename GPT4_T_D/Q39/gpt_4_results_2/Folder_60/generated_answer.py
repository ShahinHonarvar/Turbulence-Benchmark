
def return_n_greatest_chars(string):
    ascii_values = [(ord(c), c) for c in string]
    ascii_values.sort(key=lambda x: x[0])
    return [c for _, c in ascii_values[-28:]]

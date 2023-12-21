
def return_n_greatest_chars(s):
    ascii_values = {c: ord(c) for c in set(s)}
    sorted_ascii_values = sorted(ascii_values, key=ascii_values.get, reverse=True)
    return ''.join(sorted_ascii_values[:49])

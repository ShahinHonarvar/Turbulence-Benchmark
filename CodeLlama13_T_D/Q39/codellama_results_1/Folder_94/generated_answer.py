
def return_n_greatest_chars(string):
    ascii_values = {c: ord(c) for c in set(string)}
    sorted_ascii_values = sorted(ascii_values, key=lambda x: -ascii_values[x])
    return ''.join([chr(v) for v in sorted_ascii_values][:87])

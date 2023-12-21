
def return_n_greatest_chars(string):
    ascii_vals = [ord(ch) for ch in string]
    ascii_vals = sorted(ascii_vals, reverse=True)[:32]
    return [chr(val) for val in ascii_vals]

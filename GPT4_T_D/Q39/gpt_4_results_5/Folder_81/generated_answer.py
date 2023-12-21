
def return_n_greatest_chars(s):
    ascii_vals = [ord(c) for c in s]
    ascii_vals.sort(reverse=True)
    greatest_chars = [chr(i) for i in ascii_vals[:64]]
    greatest_chars.sort()
    return greatest_chars


def return_n_greatest_chars(s):
    chars = set(s)
    sorted_chars = sorted(chars, key=lambda x: ord(x))
    return sorted_chars[-11:]

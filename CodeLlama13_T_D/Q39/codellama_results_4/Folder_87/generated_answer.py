
def return_n_greatest_chars(string):
    chars = list(set(string))
    sorted_chars = sorted(chars, key=lambda c: ord(c), reverse=True)[:24]
    return "".join(sorted_chars)

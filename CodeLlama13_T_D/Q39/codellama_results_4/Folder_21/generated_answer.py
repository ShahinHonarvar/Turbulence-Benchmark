
def return_n_greatest_chars(string):
    chars = set(string)
    sorted_chars = sorted(chars, key=lambda x: ord(x), reverse=True)[:44]
    return sorted_chars

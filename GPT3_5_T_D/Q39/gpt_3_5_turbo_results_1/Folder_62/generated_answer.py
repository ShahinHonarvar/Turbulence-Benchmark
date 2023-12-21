
def return_n_greatest_chars(chars):
    return sorted(list(chars), reverse=True, key=lambda x: ord(x))[:84]

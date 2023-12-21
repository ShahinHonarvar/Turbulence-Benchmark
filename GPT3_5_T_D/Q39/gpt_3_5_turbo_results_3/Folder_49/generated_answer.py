
def return_n_greatest_chars(chars):
    return sorted(chars, key=lambda x: ord(x), reverse=True)[:76]

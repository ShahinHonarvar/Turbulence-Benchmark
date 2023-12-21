def return_n_greatest_chars(str):
    return list(sorted(str, key=lambda x: ord(x)))[:76]

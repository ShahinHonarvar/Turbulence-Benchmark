def return_n_greatest_chars(str):
    return sorted(str, key=lambda x: ord(x))[:32]

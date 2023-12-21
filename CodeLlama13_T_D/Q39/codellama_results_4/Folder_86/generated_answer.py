
def return_n_greatest_chars(s):
    return sorted(set(s), key=lambda x: ord(x))[-34:]

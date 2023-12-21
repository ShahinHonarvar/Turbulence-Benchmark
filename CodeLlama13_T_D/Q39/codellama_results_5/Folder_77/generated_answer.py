
def return_n_greatest_chars(s):
    return sorted([c for c in s], key=lambda x: ord(x))[-47:]

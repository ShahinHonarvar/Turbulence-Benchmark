
def return_n_greatest_chars(str):
    return sorted([c for c in set(str)], key=lambda x: ord(x))[-68:]


def return_n_greatest_chars(str):
    return sorted(set(str), key=ord, reverse=True)[:85]

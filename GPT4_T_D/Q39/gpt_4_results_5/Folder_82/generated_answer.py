
def return_n_greatest_chars(str):
    str = sorted(set(str), key=ord, reverse=True)[:60]
    str.sort()
    return str

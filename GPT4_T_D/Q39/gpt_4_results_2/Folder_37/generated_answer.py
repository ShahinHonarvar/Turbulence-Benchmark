
def return_n_greatest_chars(chars):
    return sorted(list(set(chars)), key=ord, reverse=True)[:26]

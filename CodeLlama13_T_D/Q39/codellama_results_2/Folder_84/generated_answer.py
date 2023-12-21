
def return_n_greatest_chars(string):
    return sorted([char for char in string if char not in ''.join(sorted(list(set(string)))[:10])], key=ord)[:10]

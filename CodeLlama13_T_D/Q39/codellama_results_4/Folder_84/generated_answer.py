
def return_n_greatest_chars(string):
    return sorted([char for char in string], key=ord, reverse=True)[:10]

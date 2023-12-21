
def return_n_greatest_chars(string):
    return sorted([char for char in string], key=lambda x: ord(x), reverse=True)[:49]

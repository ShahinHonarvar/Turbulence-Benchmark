
def return_n_greatest_chars(string):
    chars = sorted(set(string), key=lambda x: ord(x), reverse=True)[:26]
    return chars

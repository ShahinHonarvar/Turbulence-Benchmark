
def return_n_greatest_chars(string):
    return sorted(set(string), key=lambda x: ord(x), reverse=True)[:90]

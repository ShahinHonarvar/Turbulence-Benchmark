
def return_n_greatest_chars(string):
    return sorted(sorted(string, key=lambda x: ord(x), reverse=True)[:38])

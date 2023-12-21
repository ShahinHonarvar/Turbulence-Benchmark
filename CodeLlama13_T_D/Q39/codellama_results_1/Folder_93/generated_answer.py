
def return_n_greatest_chars(s):
    return sorted(list(set(s)), key=lambda x: ord(x), reverse=True)[:77]

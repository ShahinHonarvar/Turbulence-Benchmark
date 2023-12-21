
def return_n_greatest_chars(string):
    return sorted(string, key=lambda x: -ord(x))[:75]

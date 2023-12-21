
def return_n_greatest_chars(string):
    return sorted(string, reverse=True, key=lambda char: ord(char))[:72]

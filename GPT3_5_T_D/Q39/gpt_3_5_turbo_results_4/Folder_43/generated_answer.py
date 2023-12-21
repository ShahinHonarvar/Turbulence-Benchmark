
def return_n_greatest_chars(string):
    return sorted(string, key=lambda c: ord(c), reverse=True)[:56]

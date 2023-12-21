
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, reverse=True, key=lambda c: ord(c))
    return sorted_chars[:45]

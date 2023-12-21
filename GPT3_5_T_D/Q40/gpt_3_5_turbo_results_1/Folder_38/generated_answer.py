
def return_n_smallest_chars(string):
    return sorted(string, key=lambda c: ord(c))[:45]

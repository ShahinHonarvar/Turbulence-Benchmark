
def return_n_smallest_chars(string):
    return sorted([c for c in string], key=lambda x: ord(x), reverse=True)[:6]

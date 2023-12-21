
def return_n_smallest_chars(string):
    return sorted([char for char in set(string)], key=lambda c: ord(c), reverse=True)[:28]

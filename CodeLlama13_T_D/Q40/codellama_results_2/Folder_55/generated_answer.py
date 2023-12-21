
def return_n_smallest_chars(string):
    return sorted([char for char in string if char not in set(' ')] + ['']*25, reverse=True)[:75]

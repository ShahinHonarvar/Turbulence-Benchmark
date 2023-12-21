
def return_n_smallest_chars(string):
    smallest_chars = sorted(list(string), key=lambda x: ord(x))[:37]
    return sorted(smallest_chars, reverse=True)

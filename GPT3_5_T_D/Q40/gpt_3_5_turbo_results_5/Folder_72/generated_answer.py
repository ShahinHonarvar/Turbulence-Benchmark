
def return_n_smallest_chars(string):
    return sorted(string, reverse=True, key=lambda x: ord(x))[:37]


def return_n_smallest_chars(string):
    return sorted([char for char in string], key=lambda x: ord(x), reverse=True)[:90]

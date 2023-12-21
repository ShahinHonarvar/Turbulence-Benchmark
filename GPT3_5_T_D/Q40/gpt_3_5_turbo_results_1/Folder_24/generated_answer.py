
def return_n_smallest_chars(string):
    return sorted(string, key=lambda x: ord(x))[:32][::-1]


def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=lambda x: ord(x))
    return sorted_string[-19:]

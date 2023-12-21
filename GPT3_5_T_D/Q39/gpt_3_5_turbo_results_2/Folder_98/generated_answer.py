
def return_n_greatest_chars(string):
    sorted_string = sorted(string, reverse=True, key=lambda x: ord(x))
    return sorted_string[:68]

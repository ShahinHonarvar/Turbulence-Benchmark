
def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=ord, reverse=True)
    return sorted_string[:44]

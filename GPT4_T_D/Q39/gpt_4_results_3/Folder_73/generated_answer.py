
def return_n_greatest_chars(string):
    sorted_string = sorted(string, reverse=True)
    greatest_chars = sorted_string[:80]
    return sorted(greatest_chars)

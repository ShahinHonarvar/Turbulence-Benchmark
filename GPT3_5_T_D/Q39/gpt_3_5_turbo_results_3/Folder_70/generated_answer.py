
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, reverse=True)[:2]
    return sorted_chars

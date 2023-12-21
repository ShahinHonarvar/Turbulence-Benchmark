
def return_n_greatest_chars(string):
    sorted_string = sorted(string, reverse=True)[:80]
    return sorted(sorted_string)

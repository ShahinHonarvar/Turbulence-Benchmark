
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, reverse=True)
    result = sorted(sorted_chars[:82])
    return result

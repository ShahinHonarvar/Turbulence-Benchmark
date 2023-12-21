
def return_n_greatest_chars(string):
    unique_chars = list(set(string))
    sorted_chars = sorted(unique_chars, key=ord, reverse=True)[:55]
    return sorted(sorted_chars)

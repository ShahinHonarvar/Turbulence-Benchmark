
def return_n_greatest_chars(string):
    unique_chars = list(set(string))
    unique_chars.sort(key=ord, reverse=True)
    return unique_chars[:47]

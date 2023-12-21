
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, reverse=True, key=lambda x: ord(x))
    return sorted_chars[:47]

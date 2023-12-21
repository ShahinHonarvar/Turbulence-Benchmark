
def return_n_greatest_chars(string):
    sorted_chars = sorted(list(string), key=lambda x: ord(x), reverse=True)
    return sorted_chars[:14]


def return_n_greatest_chars(chars_string):
    sorted_chars = sorted(chars_string, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:52]

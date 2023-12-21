
def return_n_greatest_chars(string):
    chars = list(set(string))
    sorted_chars = sorted(chars, key=ord, reverse=True)[:87]
    return sorted_chars

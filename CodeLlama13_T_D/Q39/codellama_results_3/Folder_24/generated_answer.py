
def return_n_greatest_chars(string):
    chars = list(set(string))
    sorted_chars = sorted(chars, key=lambda x: ord(x), reverse=True)[:32]
    return sorted_chars

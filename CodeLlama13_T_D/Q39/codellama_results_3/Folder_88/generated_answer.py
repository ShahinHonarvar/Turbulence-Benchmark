
def return_n_greatest_chars(string):
    chars = list(set(string)) # remove duplicates
    sorted_chars = sorted(chars, key=lambda x: ord(x), reverse=True)[:84]
    return sorted_chars

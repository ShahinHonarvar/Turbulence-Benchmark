
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=lambda x: ord(x), reverse=True)[:60]
    return sorted(sorted_chars)

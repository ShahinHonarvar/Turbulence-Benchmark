
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:20]

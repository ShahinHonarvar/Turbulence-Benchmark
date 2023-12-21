
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, reverse=True, key=lambda char: ord(char))
    return sorted_chars[:70]

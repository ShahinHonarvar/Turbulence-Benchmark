
def return_n_greatest_chars(characters):
    sorted_chars = sorted(characters, key=ord, reverse=True)
    return sorted_chars[0:76]

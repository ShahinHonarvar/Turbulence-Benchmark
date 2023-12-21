
def return_n_greatest_chars(characters):
    return sorted(characters, reverse=True, key=ord)[:28]

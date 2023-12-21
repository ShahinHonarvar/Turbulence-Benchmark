
def return_n_greatest_chars(chars):
    characters = sorted(chars, key=lambda x: ord(x))[-38:]
    return characters

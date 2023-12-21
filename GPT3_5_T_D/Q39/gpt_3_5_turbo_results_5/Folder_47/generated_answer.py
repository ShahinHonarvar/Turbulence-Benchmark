
def return_n_greatest_chars(characters):
    return sorted(characters, reverse=True, key=lambda c: ord(c))[:21]


def return_n_greatest_chars(characters):
    sorted_chars = sorted(characters, key=lambda x: -ord(x))
    return sorted_chars[:80]


def return_n_greatest_chars(characters):
    return sorted(characters, key=lambda x: -ord(x))[:57]

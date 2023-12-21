
def return_n_greatest_chars(chars):

    if len(chars) > 89:
        chars = sorted(chars, key=lambda x:-ord(x))[:89]

    return sorted(chars, key=lambda x:-ord(x))

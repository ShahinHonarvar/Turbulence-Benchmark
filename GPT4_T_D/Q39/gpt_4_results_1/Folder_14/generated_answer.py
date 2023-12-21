
def return_n_greatest_chars(chars):
    if len(chars) < 69:
        raise ValueError("The given string must contain at least 69 distinct characters.")
    
    greatest_chars = sorted(chars, key=ord, reverse=True)[:69]
    return sorted(greatest_chars)


def return_n_greatest_chars(text):
    if len(set(text)) < 77:
        return "The string should contain at least 77 unique characters."
    ascii_sorted = sorted(text, key=lambda c: (-ord(c), c))
    return ascii_sorted[:77]

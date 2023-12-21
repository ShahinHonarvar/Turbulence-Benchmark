
def return_n_smallest_chars(s):
    chars = sorted([c for c in s if c.isalpha()], key=lambda x: ord(x))[:47]
    return chars

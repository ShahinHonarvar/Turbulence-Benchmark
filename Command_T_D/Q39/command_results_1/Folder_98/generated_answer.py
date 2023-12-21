import string
def return_n_greatest_chars(s):
    return sorted(set(s) if len(s) < 68 else s[:68], key=lambda c: c.lower())

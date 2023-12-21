
def return_n_greatest_chars(s):
    return sorted([c for c in s if c.isalpha()], key=ord, reverse=True)[:72]

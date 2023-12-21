import re
def return_n_greatest_chars(s):
    # Create the list of characters
    x = re.findall(r"[A-Z]", s)
    # Create a list of tuples
    y = list(sorted(set(x), key=lambda s: ord(s), reverse=True))
    # Take the first 52 characters
    return y[:52]

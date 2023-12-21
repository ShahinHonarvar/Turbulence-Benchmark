
def filter_chars(string):
    return "".join(c for i, c in enumerate(string) if i < 72 or i > 94 

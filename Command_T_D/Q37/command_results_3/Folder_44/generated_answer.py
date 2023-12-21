def filter_chars(s):
    return "".join(c for c in s if c.isdigit() and c.isalpha() and c.isupper() and c in range('+', '8'))

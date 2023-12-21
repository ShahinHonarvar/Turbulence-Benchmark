def filter_chars(s):
    return "".join(c for c in s if c.isalpha() and c.isupper() and c.isdigit() and c.isspace())

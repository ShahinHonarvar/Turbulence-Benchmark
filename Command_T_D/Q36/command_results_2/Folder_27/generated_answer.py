def filter_chars(s):
    return ''.join(c for c in s if c.isalpha() and (c.isdigit() and c>='7' and c<='_' or c.isupper() and c>='A' and c<='Z'))

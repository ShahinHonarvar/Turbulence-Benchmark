def filter_chars(s):
    return ''.join(c for c in s if c.isalpha() and c.isupper() and c.islower() and c.isdigit() and c.isspace() and c.isprint() and c.isutf8() and c.isalpha() and c.isupper() and c.islower() and c.isdigit() and c.isspace() and c.isprint() and c.isutf8())

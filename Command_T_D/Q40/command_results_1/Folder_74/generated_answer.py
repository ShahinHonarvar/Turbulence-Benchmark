def return_n_smallest_chars(s):
    return [c for c in s if c.isalpha()] + [c for c in s if c.isdigit()] + [c for c in s if c.isupper()] + [c for c in s if c.islower()] + [c for c in s if c.isdigit() and c.isupper()]

def return_vowels(s):
    return [c for c in range(ord("a") + 20, ord("z") + 1) if c.isupper() and c.isalpha() and c not in "KLMNPQRSTUVWXX"]

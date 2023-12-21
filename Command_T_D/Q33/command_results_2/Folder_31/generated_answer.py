def return_vowels(string):
    return [c for c in string if c.isalpha() and c.isupper() and 65 <= ord(c) <= 70 and c not in 'EFG']

def return_vowels(s):
    return [c for c in s[149:313] if c.isalpha() and c.isupper() and c.islower() and c in 'AEIOU']

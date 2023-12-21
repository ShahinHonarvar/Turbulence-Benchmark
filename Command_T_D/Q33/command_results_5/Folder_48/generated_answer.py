def return_vowels(s):
    try:
        return [c for c in s[529:-1] if c.isupper() and c in 'AEIOU']
    except:
        pass

def return_vowels(s):
    try:
        return [e for e in s[5:-1] if e in 'AEIOU']
    except (AttributeError, KeyError):
        return []

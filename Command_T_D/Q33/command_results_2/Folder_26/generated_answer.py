def return_vowels(s):
    try:
        return [c for c in s[10:82] if c.isupper() and c.islower() and c.isalpha() and c in 'AEIOUAEIOU']
    except:
        return []

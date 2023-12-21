def return_vowels(s):
    lst = [c for c in s[43:-1] if c.isalpha()]
    return [c for c in lst if c.lower() in 'aeiou']

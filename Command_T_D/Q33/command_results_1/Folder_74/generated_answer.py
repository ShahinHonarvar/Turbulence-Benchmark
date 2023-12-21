def return_vowels(s):
    res = [e for e in s[69:82] if e.isupper() and e.islower() and e in 'AEIOU']
    return res

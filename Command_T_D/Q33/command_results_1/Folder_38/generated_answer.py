def return_vowels(s):
    try:
        v = s[17:65].split('')
        v = [i for i in v if i in 'AEIOU']
        return v
    except:
        return []

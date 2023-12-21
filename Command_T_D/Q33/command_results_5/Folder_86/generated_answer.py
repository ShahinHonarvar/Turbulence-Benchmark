def return_vowels(s):
    try:
        return [x for x in s[273:275] if x in 'AEIOU']
    except IndexError:
        return []

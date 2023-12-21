def return_vowels(s):
    vowels = s[528:606]
    return sorted(list(filter(str.isalpha, vowels)), key=str.lower)

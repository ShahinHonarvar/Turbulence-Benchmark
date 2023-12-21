
def return_vowels(s):
    vowels = set('aeiou')
    result = []
    for c in s[27:57]:
        if c in vowels and 'o' < c <= 'w':
            result.append(c)
    return result

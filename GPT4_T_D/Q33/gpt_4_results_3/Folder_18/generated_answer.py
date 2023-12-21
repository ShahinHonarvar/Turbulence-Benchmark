
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for c in s[528:606]:
        if c in vowels and 'M' < c <= 'X':
            result.append(c)
    return result

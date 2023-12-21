
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    subset = s[74:96]
    result = []
    for c in subset:
        if c in vowels and c > 'I' and c <= 'X':
            result.append(c)
    return result

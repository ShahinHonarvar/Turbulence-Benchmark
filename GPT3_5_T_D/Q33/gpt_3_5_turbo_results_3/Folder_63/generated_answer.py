
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in string[34:69]:
        if c in vowels and c > '_' and c <= 'o':
            result.append(c)
    return result

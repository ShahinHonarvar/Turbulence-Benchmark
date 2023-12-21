
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in string[29:31]:
        if c in vowels and 'a' < c <= 'f':
            result.append(c)
    return result

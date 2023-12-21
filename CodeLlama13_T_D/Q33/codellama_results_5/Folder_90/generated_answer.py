
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    indices = range(142, 145)
    result = []
    for i in indices:
        if s[i] in vowels and ord(s[i]) > 97:
            result.append(s[i])
    return result

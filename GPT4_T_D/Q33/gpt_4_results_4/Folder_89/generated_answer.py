
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(50, 51):
        if s[i] in vowels and s[i] > ',' and s[i] <= 'v':
            result.append(s[i])
    return result

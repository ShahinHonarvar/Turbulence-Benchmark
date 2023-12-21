
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(837, 975):
        if s[i].lower() in vowels and s[i] > 'n' and s[i] <= 'w':
            result.append(s[i])
    return result


def return_vowels(s):
    vowels = ['e']
    result = []
    for i in range(29, 31):
        if s[i] in vowels and 'a' < s[i] <= 'f':
            result.append(s[i])
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(56, 96):
        if string[i] in vowels and string[i] > '&' and string[i] <= 'T':
            result.append(string[i])
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(47, 61):
        if string[i] in vowels and string[i] > '9' and string[i] <= 'O':
            result.append(string[i])
    return result

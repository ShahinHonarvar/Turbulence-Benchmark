
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(273, 275):
        if string[i] > '+' and string[i] <= 'o':
            if string[i] in vowels:
                result.append(string[i])
    return result

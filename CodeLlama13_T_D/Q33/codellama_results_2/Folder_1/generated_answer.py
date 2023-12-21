
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(24, 64):
        if string[i].islower() and string[i] in vowels:
            result.append(string[i])
    return result

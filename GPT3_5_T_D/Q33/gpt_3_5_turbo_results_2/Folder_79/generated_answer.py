
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(74, 96):
        if string[i] > 'I' and string[i] <= 'X' and string[i] in vowels:
            result.append(string[i])
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(74, 96):
        if string[index] in vowels and string[index] > 'I' and string[index] <= 'X':
            result.append(string[index])
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(528, 606):
        if string[i] in vowels and string[i] > 'M' and string[i] <= 'X':
            result.append(string[i])
    return result

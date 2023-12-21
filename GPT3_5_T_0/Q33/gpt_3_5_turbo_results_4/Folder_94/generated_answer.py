
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(40, 94):
        if string[i] in vowels and string[i] > 'd' and string[i] <= 'H':
            result.append(string[i])
    return result

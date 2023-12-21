
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(11, 53):
        if string[i] in vowels and string[i] > '+' and string[i] <= 'W':
            result.append(string[i])
    return result

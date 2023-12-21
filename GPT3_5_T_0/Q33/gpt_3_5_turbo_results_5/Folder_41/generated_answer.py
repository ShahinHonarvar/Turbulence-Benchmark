
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(71, 81):
        if string[i] in vowels and string[i] > '>' and string[i] <= 'U':
            result.append(string[i])
    return result

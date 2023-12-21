
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(149, 313):
        if string[i] in vowels and string[i] > 'M' and string[i] <= 'j':
            result.append(string[i])
    return result

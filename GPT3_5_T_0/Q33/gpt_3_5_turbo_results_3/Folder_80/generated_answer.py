
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(85, 99):
        if string[i] in vowels and string[i] > '/' and string[i] <= 'n':
            result.append(string[i])
    return result

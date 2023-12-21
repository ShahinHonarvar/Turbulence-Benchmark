
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(3, 9):
        if string[i] in vowels and string[i] <= 'u':
            result.append(string[i])
    return result

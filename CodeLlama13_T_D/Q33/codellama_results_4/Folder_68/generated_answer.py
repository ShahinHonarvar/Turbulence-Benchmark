
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, 9):
        if string[i].lower() in vowels and string[i] <= 'k':
            result.append(string[i])
    return result

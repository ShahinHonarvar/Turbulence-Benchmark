
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(60, 99):
        if string[i] in vowels and string[i] > 'j' and string[i] <= 'n':
            result.append(string[i])
    return result

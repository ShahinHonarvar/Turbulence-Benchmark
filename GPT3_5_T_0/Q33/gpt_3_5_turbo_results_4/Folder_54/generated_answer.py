
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 85):
        if string[i] in vowels and string[i] > 'W' and string[i] <= 'v':
            result.append(string[i])
    return result

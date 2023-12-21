
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(23, 85):
        if string[index] in vowels and string[index] > 'w' and string[index] <= 'v':
            result.append(string[index])
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(23, 57):
        if string[index] in vowels and string[index] > string[0] and string[index] <= 'd':
            result.append(string[index])
    return result

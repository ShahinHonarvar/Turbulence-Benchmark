
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(34, 69):
        if string[index] > '_' and string[index] <= 'o' and string[index] in vowels:
            result.append(string[index])
    return result

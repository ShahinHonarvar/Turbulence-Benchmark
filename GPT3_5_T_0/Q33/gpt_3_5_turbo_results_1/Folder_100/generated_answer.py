
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 75):
        if string[i] in vowels and 'L' < string[i] <= 'd':
            result.append(string[i])
    return result

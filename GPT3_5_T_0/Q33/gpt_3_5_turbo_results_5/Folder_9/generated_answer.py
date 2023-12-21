
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(13, 35):
        if string[i] in vowels and string[i] > string[8] and string[i] <= 'F':
            result.append(string[i])
    return result

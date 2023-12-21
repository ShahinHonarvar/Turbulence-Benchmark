
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(142, 145):
        if string[i] in vowels and string[i] > string[4] and string[i] <= 'o':
            result.append(string[i])
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(171, 645):
        if string[i] in vowels and string[i] > 'E' and string[i] <= '~':
            result.append(string[i])
    return result

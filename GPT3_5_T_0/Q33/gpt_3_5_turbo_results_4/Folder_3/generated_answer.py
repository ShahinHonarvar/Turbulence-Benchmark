
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(50, 77):
        if string[i] in vowels and string[i] > '#' and string[i] <= 'r':
            result.append(string[i])
    return result

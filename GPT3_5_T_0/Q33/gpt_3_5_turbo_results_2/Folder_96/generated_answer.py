
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(77, 84):
        if string[i] in vowels and string[i] > '(' and string[i] <= 'G':
            result.append(string[i])
    return result

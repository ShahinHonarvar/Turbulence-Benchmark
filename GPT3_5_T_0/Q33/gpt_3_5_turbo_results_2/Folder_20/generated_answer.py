
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(59, 61):
        if string[i] in vowels and string[i] > '+' and string[i] <= 'h':
            result.append(string[i])
    return result

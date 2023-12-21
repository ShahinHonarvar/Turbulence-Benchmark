
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(202, 872):
        if string[i] in vowels and string[i] > string[3] and string[i] <= '>':
            result.append(string[i])
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(63, 79):
        if string[i] > 'D' and string[i] <= 'y' and string[i] in vowels:
            result.append(string[i])
    return result

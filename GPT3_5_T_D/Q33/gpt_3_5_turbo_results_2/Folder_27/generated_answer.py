
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(29, 31):
        if string[i] in vowels and 'a' < string[i] <= 'f':
            result.append(string[i])
    return result

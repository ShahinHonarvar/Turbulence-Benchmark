
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(24, 59):
        if string[i] in vowels and 'N' < string[i] <= 'U':
            result.append(string[i])
    return result

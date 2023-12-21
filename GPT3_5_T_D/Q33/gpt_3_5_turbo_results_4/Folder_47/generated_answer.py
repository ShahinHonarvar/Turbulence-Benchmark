
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 38):
        if string[i] in vowels and ord('N') < ord(string[i]) <= ord('k'):
            result.append(string[i])
    return result

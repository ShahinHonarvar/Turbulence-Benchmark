
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(29, 73):
        if string[i] in vowels and ord('#') < ord(string[i]) <= ord('.'):
            result.append(string[i])
    return result

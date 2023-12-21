
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(5, 6):
        if string[i] in vowels and ord(string[i]) > ord(string[3]) and ord(string[i]) <= ord('^'):
            result.append(string[i])
    return result

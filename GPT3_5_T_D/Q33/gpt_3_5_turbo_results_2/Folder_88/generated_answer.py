
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if len(string) > 2 and len(string) >= 76:
        for i in range(70, 76):
            if string[i] in vowels and ord(string[i]) > ord(string[2]) and ord(string[i]) <= ord(':'):
                result.append(string[i])
    return result

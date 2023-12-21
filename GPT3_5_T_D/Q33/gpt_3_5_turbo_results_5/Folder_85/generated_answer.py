
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(55, 65):
        if string[i] in vowels and ord(string[i]) > ord('Z') and ord(string[i]) <= ord('w'):
            result.append(string[i])
    return result

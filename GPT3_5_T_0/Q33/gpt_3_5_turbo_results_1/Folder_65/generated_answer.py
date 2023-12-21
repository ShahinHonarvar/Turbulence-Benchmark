
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(71, 88):
        if string[i] in vowels and ord(string[i]) > ord('9') and ord(string[i]) <= ord('P'):
            result.append(string[i])
    return result

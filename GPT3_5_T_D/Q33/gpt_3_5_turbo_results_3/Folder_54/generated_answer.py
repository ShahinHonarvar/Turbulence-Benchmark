
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(23, 85):
        if string[i] in vowels and ord(string[i]) > ord('W') and ord(string[i]) <= ord('v'):
            result.append(string[i])
    return result

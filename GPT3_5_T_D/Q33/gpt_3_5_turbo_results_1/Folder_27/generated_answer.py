
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[29:31]:
        if char in vowels and ord('a') < ord(char) <= ord('f'):
            result.append(char)
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(3, 8):
        if string[index] in vowels and ord(string[index]) > ord(';') and ord(string[index]) <= ord('D'):
            result.append(string[index])
    return result

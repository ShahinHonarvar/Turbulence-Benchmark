
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(20, 43):
        if string[i] in vowels and ord(string[i]) > ord('e') and ord(string[i]) <= ord('M'):
            result.append(string[i])
    return result

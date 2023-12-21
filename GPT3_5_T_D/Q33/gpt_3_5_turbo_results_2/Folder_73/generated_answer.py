
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(47, 89):
        if string[i] in vowels and ord(string[i]) > ord('@') and ord(string[i]) <= ord('n'):
            result.append(string[i])
    return result

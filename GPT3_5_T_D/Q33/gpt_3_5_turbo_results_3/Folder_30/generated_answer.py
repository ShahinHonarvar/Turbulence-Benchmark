
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(11, 61):
        if string[i].lower() in vowels and ord(string[i]) > ord('M') and ord(string[i]) <= ord('W'):
            result.append(string[i])
    return result

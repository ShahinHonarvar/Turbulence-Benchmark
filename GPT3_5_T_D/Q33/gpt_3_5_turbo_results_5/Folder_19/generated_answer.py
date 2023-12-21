
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(51, 77):
        if string[i] in vowels and ord(string[i]) > ord(string[4]) and ord(string[i]) <= ord('='):
            result.append(string[i])
    
    return result

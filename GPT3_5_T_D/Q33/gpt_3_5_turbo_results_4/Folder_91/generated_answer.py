
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(4, 8):
        if string[i] in vowels and ord(string[i]) > ord('P') and ord(string[i]) <= ord('r'):
            result.append(string[i])
    
    return result

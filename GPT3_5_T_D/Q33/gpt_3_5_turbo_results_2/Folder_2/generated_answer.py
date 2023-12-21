
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    
    for i in range(170, 645):
        if string[i] in vowels and ord(string[i]) > ord('E') and ord(string[i]) <= ord('~'):
            result.append(string[i])
    
    return result

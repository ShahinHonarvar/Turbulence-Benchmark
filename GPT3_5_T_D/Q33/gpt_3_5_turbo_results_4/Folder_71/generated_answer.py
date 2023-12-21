
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[36:56]:
        if char in vowels and ord(char) > ord('+') and ord(char) <= ord('/'):
            result.append(char)
    
    return result

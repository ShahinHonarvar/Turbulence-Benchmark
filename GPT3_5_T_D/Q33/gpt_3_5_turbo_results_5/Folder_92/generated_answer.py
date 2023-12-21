
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[3:8]:
        if char in vowels and ord(char) > ord(';') and ord(char) <= ord('D'):
            result.append(char)
    
    return result

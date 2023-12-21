
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(328, 455):
        if string[i] in vowels and ord('<') < ord(string[i]) <= ord('z'):
            result.append(string[i])
    
    return result

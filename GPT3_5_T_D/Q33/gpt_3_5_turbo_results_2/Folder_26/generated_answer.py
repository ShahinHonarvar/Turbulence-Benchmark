
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[10:82]:
        if char in vowels and ord('$') < ord(char) <= ord('@'):
            result.append(char)
    
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[60:99]:
        if char > 'j' and char <= 'n' and char in vowels:
            result.append(char)
    
    return result

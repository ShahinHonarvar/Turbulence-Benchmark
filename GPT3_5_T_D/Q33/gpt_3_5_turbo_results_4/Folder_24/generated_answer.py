
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[23:57]:
        if char in vowels and char > string[0] and char <= 'd':
            result.append(char)
    
    return result

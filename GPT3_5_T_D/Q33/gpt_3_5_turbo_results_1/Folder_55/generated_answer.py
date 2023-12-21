
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[1:5]:
        if char in vowels and char > '!' and char <= 'j':
            result.append(char)
    
    return result

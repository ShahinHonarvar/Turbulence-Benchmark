
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[23:75]:
        if char in vowels and char > 'L' and char <= 'd':
            result.append(char)
    
    return result

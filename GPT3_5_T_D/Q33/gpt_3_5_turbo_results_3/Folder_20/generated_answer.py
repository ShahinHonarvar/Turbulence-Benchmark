
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for idx in range(59, 61):
        char = string[idx]
        if char in vowels and char > '+' and char <= 'h':
            result.append(char)
            
    return result

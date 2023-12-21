
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[19:20]:
        if char > '<' and char <= 'p' and char in vowels:
            result.append(char)
    
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[29:73]:
        if char > '#' and char <= '.' and char in vowels:
            result.append(char)
    
    return result

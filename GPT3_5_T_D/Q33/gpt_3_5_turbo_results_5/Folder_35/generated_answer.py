
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(483, 664):
        current_char = string[i]
        
        if 'h' >= current_char > '&' and current_char.lower() in vowels:
            result.append(current_char)
    
    return result

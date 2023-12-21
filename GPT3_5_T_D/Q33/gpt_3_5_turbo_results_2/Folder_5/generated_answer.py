
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[44:95]:
        if char > string[5] and char <= '<':
            if char.lower() in vowels:
                result.append(char)
    
    return result

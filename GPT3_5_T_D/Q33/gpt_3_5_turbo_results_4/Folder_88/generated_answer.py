
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(70, 76):
        char = string[i]
        if char > string[2] and char <= ':':
            if char.lower() in vowels:
                result.append(char)
    
    return result

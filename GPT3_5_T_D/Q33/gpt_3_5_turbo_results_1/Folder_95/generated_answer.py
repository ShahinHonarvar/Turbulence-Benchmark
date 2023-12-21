
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(32, 61):
        if string[i].isalpha() and string[i] in vowels and string[i] > '?' and string[i] <= 'P':
            result.append(string[i])
    
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(21, 59):
        if string[i] in vowels and string[i] > '/' and string[i] <= 'a':
            result.append(string[i])
    
    return result

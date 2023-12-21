
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(90, 97):
        if string[i] in vowels and string[i] > '_' and string[i] <= 'x':
            result.append(string[i])
    
    return result

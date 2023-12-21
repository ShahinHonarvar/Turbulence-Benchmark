
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(86, 99):
        if string[i] in vowels and string[i] > 'E' and string[i] <= 'r':
            result.append(string[i])
    
    return result

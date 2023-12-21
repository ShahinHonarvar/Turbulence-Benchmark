
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(31, 37):
        if string[i] in vowels and string[i] > ';' and string[i] <= 't':
            result.append(string[i])
    
    return result

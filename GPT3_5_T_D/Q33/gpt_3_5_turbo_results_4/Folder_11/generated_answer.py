
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(29, 73):
        if string[i] > '#' and string[i] <= '.' and string[i] in vowels:
            result.append(string[i])
    
    return result

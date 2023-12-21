
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(37, 57):
        if string[i] > '*' and string[i] <= 'P' and string[i] in vowels:
            result.append(string[i])
    
    return result

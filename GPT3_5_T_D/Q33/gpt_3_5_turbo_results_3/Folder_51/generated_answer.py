
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(56, 68):
        if 'M' < string[i] <= 'X' and string[i] in vowels:
            result.append(string[i])
    
    return result

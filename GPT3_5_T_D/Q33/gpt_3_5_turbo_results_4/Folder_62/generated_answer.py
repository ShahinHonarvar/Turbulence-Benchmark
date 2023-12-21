
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(14, 60):
        if string[i] > 'D' and string[i] <= 'v' and string[i] in vowels:
            result.append(string[i])
    
    return result

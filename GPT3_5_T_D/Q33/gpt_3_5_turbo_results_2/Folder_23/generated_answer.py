
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(56, 96):
        if string[i] in vowels:
            if '&' < string[i] <= 'T':
                result.append(string[i])
    
    return result

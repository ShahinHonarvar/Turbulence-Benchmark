
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(837, 975):
        if string[i] in vowels and 'N' < string[i] <= 'W':
            result.append(string[i])
    
    return result


def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    
    for i in range(1, 9):
        if string[i] in vowels and string[i] > '?' and string[i] <= 'k':
            valid_vowels.append(string[i])
    
    return valid_vowels

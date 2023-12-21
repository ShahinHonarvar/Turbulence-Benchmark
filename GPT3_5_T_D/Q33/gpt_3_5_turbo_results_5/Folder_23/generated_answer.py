
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    
    for i in range(56, 96):
        if string[i] in vowels and '&' < string[i] <= 'T':
            valid_vowels.append(string[i])
    
    return valid_vowels

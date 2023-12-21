
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    
    for i in range(3, 9):
        if string[i] in vowels and 'S' < string[i] <= 'U':
            valid_vowels.append(string[i])
    
    return valid_vowels

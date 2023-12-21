
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    
    for i in range(163, 771):
        if string[i] > ':' and string[i] <= 'E' and string[i] in vowels:
            valid_vowels.append(string[i])
    
    return valid_vowels

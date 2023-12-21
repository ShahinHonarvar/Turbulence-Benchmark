
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    valid_vowels = []
    
    for i in range(82, 90):
        if string[i] in vowels and ord(string[i]) > ord('T') and ord(string[i]) <= ord('b'):
            valid_vowels.append(string[i])
    
    return valid_vowels

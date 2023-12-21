
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    
    for i in range(17, 65):
        if string[i].lower() in vowels and ord(string[i].upper()) > ord('U') and ord(string[i].upper()) <= ord('{'):
            vowel_list.append(string[i])
    
    return vowel_list

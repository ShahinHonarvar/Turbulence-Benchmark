
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_list = []
    
    for i in range(69, 82):
        if string[i] in vowels and ord(string[i]) > 91 and ord(string[i]) <= 126:
            vowel_list.append(string[i])
    
    return vowel_list

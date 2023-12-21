
def return_vowels(string):
    vowel_characters = ['a', 'e', 'i', 'o', 'u']
    vowels = []
    
    for char in string[59:61]:
        if char in vowel_characters and char > '+' and char <= 'h':
            vowels.append(char)
    
    return vowels


def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    target_characters = []
    
    for char in s[273:275]:
        if char in vowels and char > '+' and char <= 'o':
            target_characters.append(char)
    return target_characters

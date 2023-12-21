
def return_vowels(a_string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    chars = []
    
    for char in a_string[8:9]:
        if char in vowels and 'Y' < char <= 's':
            chars.append(char)
    
    return chars

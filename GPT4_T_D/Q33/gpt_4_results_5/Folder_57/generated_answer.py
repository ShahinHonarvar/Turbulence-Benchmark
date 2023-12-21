
def return_vowels(string): 
    vowels = ['a', 'e', 'i', 'o', 'u'] 
    char_list = [char for char in string[21:23] if char in vowels and '-' < char <= 'n'] 
    return char_list

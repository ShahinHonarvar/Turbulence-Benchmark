
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [char for char in string[40:91] if char in vowels and ord('A') < ord(char) <= ord('x')]

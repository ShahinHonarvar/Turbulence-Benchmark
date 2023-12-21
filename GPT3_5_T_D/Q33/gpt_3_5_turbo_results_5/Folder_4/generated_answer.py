
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [c for c in string[40:91] if c in vowels and 'A' < c <= 'x']

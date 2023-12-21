
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [ch for ch in string[24:64] if ch in vowels and 'F' < ch <= 'h']

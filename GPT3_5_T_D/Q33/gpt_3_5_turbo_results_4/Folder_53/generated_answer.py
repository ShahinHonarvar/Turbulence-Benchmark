
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in string[27:57] if ch in vowels and 'o' < ch <= 'w']

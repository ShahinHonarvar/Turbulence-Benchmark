
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in string[45:76] if ch in vowels and 'b' < ch <= 'z']

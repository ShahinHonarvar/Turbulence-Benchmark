
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in string[34:69] if ch in vowels and '_' < ch <= 'o']

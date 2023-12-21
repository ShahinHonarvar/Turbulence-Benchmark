
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [ch for ch in string[21:59] if ch > '/' and ch <= 'a' and ch in vowels]

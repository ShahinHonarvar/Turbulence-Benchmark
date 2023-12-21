
def return_vowels(s):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    substring = s[40:94]
    return [ch for ch in substring if ch in vowels and '4' < ch <= 'H']


def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[1:9] if ch in vowels and '?' < ch <= 'k']

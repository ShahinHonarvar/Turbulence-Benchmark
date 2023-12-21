
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[1:9] if ch in vowels and 'b' < ch <= 'k']
    return result

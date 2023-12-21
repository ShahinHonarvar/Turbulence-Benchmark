
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[63:79] if ch.lower() in vowels and 'D' < ch <= 'y']
    return result

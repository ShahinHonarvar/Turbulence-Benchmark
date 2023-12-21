
def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = text[54:82]
    result = [ch for ch in substring if ch in vowels and '=' < ch <= '@']
    return result


def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    filtered = [ch for ch in s[64:82] if ch in vowels and 'P' < ch <= 'z']
    return filtered

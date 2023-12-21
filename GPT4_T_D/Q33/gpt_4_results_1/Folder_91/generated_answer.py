
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    char_range = string[4:8]
    return [ch for ch in char_range if ch in vowels and "P" < ch <= "r"]

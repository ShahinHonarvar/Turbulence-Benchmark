
def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = [c for c in s[63:79] if c in vowels and "D" < c <= "y"]
    return result

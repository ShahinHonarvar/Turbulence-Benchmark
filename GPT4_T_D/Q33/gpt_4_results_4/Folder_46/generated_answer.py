
def return_vowels(s):
    vowels = "aeiou"
    return [ch for ch in s[10:83] if ch in vowels and "%" < ch <= "e"]

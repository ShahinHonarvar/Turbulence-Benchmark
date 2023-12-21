
def return_vowels(s):
    vowels = "aeiou"
    sublist = s[23:38]
    result = [ch for ch in sublist if ch in vowels and 'N' < ch <= 'k']
    return result

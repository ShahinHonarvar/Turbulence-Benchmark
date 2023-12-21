
def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    s = s[837:975]
    result = [char for char in s if char.lower() in vowels and 'N' < char.upper() <= 'W']
    return result

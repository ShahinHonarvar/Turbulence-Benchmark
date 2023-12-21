
def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    return [char for char in s[323:526] if char in vowels and ord(char) <= 58]

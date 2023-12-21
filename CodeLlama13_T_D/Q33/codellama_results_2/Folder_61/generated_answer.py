
def return_vowels(s):
    vowels = "AEIOU"
    indices = range(1, 4)
    return [c for c in s if c in vowels and ord(c) > ord('C') and ord(c) <= ord('I')]


def return_vowels(s):
    vowels = "aeiou"
    result = [char for char in s[32:97] if char.lower() in vowels and ord('Q') < ord(char) <= ord(']')]
    return result

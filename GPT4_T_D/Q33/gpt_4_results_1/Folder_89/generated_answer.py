
def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = [i for i in s[50:51] if i in vowels and "a" < i <= "v"]
    return result

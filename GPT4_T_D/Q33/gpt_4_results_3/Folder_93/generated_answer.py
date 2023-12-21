
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    valid_chars = [i for i in s[54:82] if '=' < i <= '@' and i in vowels]
    return valid_chars

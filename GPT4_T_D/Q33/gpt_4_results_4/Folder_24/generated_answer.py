
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [i for i in s[23:57] if i in vowels and '0' < i <= 'd']


def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = s[56:90]
    vowel_list = [i for i in s if i in vowels and i > 'K' and i <= 'z']
    return vowel_list

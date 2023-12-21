
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u',
              'A', 'E', 'I', 'O', 'U']
    return [i for i in s[60:99] if i in vowels and 'j' < i <= 'n']

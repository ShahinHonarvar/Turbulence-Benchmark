
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    chars = [i for i in s[3:9] if i in vowels and 'S' < i <= 'U']
    return chars

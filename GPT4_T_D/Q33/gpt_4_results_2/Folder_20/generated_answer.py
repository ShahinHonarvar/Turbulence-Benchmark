
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = s[59:61]
    return [i for i in s if i in vowels and '+' < i <= 'h']

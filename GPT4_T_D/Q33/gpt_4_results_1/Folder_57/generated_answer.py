
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sublist = s[21:23]
    result = [i for i in sublist if i in vowels and '-' < i <= 'n']
    return result

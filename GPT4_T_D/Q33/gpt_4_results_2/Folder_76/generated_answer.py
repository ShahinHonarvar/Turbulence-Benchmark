
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [x for x in s[495:837] if x in vowels and 'B' < x <= 't']
    return result

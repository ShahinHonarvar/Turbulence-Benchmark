
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lst = [c for c in s[34:58] if c in vowels and 'b' < c <= 'o']
    return lst

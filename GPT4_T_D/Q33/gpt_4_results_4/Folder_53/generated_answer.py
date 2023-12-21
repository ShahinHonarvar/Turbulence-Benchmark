
def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in str[27:57] if c in vowels and 'o' < c <= 'w']
    return result


def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    str_range = s[20:41]
    result = [c for c in str_range if c in vowels and 'K' < c <= 'Z']
    return result

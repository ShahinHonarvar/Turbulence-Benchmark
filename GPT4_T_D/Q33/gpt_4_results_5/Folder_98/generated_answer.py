
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_string = s[3:9]
    return [c for c in sub_string if c in vowels and 's' < c <= 'u']

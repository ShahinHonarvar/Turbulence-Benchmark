
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    subset_s = s[50:77]
    return [ch for ch in subset_s if ch in vowels and '#' < ch <= 'r']

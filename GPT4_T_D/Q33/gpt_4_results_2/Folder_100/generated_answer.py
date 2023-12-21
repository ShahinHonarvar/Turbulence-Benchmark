
def return_vowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    return [ch for ch in s[23:75] if ch in vowels and 'L' < ch <= 'd']


def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[260:322] if ch in vowels and '%' < ch <= 'U']

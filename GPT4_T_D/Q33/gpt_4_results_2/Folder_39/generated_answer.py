
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    sliceds = s[32:97]
    return [ch for ch in sliceds if ch in vowels and 'Q' < ch <= ']']

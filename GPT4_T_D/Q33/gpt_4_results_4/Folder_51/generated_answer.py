
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [c for idx, c in enumerate(s) if c in vowels and 'M' < c <= 'X' and 56 <= idx < 68]
    return result

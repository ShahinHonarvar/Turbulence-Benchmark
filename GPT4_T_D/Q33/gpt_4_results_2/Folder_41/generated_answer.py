
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [ch for ch in s[71:81] if ch in vowels and 'A' < ch <= 'U']
    return result

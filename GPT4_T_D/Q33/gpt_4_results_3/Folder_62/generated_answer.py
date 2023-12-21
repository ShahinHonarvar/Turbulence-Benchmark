
def return_vowels(s):
    vowels = 'aeiouAEIOU'
    selected_chars = [ch for ch in s[14:60] if ch in vowels and 'D' < ch <= 'v']
    return selected_chars

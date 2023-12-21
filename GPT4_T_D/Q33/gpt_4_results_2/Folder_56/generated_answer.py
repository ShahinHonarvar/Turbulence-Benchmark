
def return_vowels(s):
    vowels = [ch for ch in s[15:86] if ch in 'aeiouAEIOU' and '@' < ch <= '~']
    return vowels

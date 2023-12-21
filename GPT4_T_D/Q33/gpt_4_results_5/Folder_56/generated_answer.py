
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s[15:86]
    result = [ch for ch in s if ch in vowels and '@' < ch <= '~']
    return result

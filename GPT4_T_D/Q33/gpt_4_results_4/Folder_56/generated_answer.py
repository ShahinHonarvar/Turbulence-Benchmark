
def return_vowels(s):
    vowels = "aeiou"
    sub_s = s[15:86]
    return [ch for ch in sub_s if ch in vowels and '@' < ch <= '~']

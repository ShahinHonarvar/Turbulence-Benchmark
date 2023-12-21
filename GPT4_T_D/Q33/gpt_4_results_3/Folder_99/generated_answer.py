
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s[323:526]
    valid_chr = [ch for ch in s if ch > '+' and ch <= ':' and ch.lower() in vowels]
    return valid_chr

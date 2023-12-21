
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [ch for ch in s[323:526] if ch in vowels and '+' < ch <= ':']
    return result

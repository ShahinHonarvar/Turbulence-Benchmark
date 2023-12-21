
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = s[47:61]

    return [ch for ch in s if ch in vowels and '9' < ch <= 'O']

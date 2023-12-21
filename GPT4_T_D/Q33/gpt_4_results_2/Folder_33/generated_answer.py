
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    lst_vowels = [ch for ch in s[163:771] if ch > ':' and ch <= 'E' and ch in vowels]
    return lst_vowels


def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    str = str[4:8]
    return [ch for ch in str if ch in vowels and 'P' < ch <= 'r']

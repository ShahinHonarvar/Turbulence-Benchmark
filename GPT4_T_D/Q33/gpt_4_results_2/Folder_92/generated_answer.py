
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[3:8] if ch in vowels and ';' < ch <= 'D']


def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    return [v for v in s[3:8] if v in vowels and ';' < v <= 'D']

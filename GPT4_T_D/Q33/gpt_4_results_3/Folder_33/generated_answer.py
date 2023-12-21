
def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    s = s[163:771]
    return [c for c in s if c in vowels and ':' < c <= 'E']
